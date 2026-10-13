# -*- coding: utf-8 -*-
"""从 Hexo/NexT 静态文章页(gh-pages)提取内容并转换为 Markdown。
用法:
  python ghpages_to_md.py --scan              # 只扫描各篇字段，不写文件
  python ghpages_to_md.py --out <目录>        # 转换并写入 <目录> 下的 .md
"""
import argparse
import glob
import os
import re
import sys
from bs4 import BeautifulSoup

ROOT = r"C:\Users\zuorn\Downloads\zuorn-gh-pages"


def pick_date(meta, itemtype):
    """从 <time itemprop> 的 datetime 或 <meta itemprop/property> 里取日期。"""
    for t in meta.find_all("time"):
        ip = t.get("itemprop", "")
        if itemtype in ip.split():
            d = t.get("datetime")
            if d:
                return d
    for m in meta.find_all("meta"):
        if itemtype in (m.get("itemprop") or "").split():
            d = m.get("datetime") or m.get("content")
            if d:
                return d
    for m in meta.find_all("meta"):
        if m.get("property") in ("article:published_time",):
            d = m.get("content")
            if d:
                return d
    return None


def parse_post(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        soup = BeautifulSoup(f.read(), "lxml")

    title_el = soup.select_one("h1.post-title")
    title = title_el.get_text(strip=True) if title_el else os.path.basename(os.path.dirname(path))

    date = pick_date(soup, "dateCreated") or pick_date(soup, "datePublished")
    updated = pick_date(soup, "dateModified")

    categories = []
    for a in soup.select('.post-meta a[href*="/categories/"]'):
        t = a.get_text(strip=True)
        if t and t not in categories:
            categories.append(t)

    tags = []
    for a in soup.select(".post-footer .post-tags a[rel='tag'], .post-meta a[rel='tag']"):
        t = a.get_text(strip=True).lstrip("#").strip()
        if t and t not in tags:
            tags.append(t)

    body = soup.select_one(".post-body")
    return {
        "title": title,
        "date": date,
        "updated": updated,
        "categories": categories,
        "tags": tags,
        "body": body,
    }


def inline_to_md(node, in_code=False):
    """把行内节点转为 markdown 文本。"""
    if node is None:
        return ""
    if isinstance(node, list):
        return "".join(inline_to_md(n, in_code) for n in node)
    if isinstance(node, str):
        return node
    name = node.name
    if name is None:
        return node.get_text()
    if name == "a":
        href = node.get("href", "")
        txt = inline_to_md(node.contents, in_code)
        # 摘要分割锚点
        if node.get("id") == "more":
            return "\n\n<!-- more -->\n\n"
        if not txt or not href:
            return txt
        return "[{}]({})".format(txt, href)
    if name == "img":
        src = node.get("src", "")
        alt = node.get("alt", "") or ""
        return "![{}]({})".format(alt, src)
    if name == "strong" or name == "b":
        t = inline_to_md(node.contents, in_code)
        return "**{}**".format(t) if t else ""
    if name == "em" or name == "i":
        t = inline_to_md(node.contents, in_code)
        return "*{}*".format(t) if t else ""
    if name == "code" and not in_code:
        t = node.get_text()
        return "`{}`".format(t)
    if name == "br":
        return "\n"
    if name == "sup" or name == "sub":
        return node.get_text()
    # 其它标签：递归取文本
    return inline_to_md(node.contents, in_code)


def render_inline(parent):
    """渲染一个容器里连续的行内内容（把多个节点拼起来）。"""
    parts = []
    for child in parent.contents:
        parts.append(inline_to_md(child))
    # 去掉多余空白行（markdown 段落内不应有多余空行）
    text = "".join(parts)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def render_highlight(figure):
    """渲染 hexo highlight 代码块 `<figure class="highlight lang">`。"""
    lang = "text"
    cls = figure.get("class", [])
    if len(cls) >= 2:
        lang = cls[1]
    code_td = figure.select_one("td.code pre") or figure.select_one("pre")
    lines = []
    if code_td is not None:
        for ln in code_td.select("span.line"):
            lines.append(ln.get_text())
        if not lines:
            raw = code_td.get_text()
            lines = [l for l in raw.split("\n")]
    body = "\n".join(lines).strip("\n")
    return "```{}\n{}\n```\n\n".format(lang, body)


def render_block(node):
    """渲染一个块级元素为 markdown。"""
    name = node.name
    if name == "p":
        return render_inline(node) + "\n\n"
    if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(name[1])
        return "#" * level + " " + render_inline(node) + "\n\n"
    if name == "figure" and "highlight" in (node.get("class") or []):
        return render_highlight(node)
    if name == "pre":
        lang = "text"
        code = node.find("code")
        if code:
            txt = code.get_text().strip("\n")
        else:
            txt = node.get_text().strip("\n")
        return "```{}\n{}\n```\n\n".format(lang, txt)
    if name == "blockquote":
        inner = render_children(node)
        inner = "\n".join("> " + l if l else ">" for l in inner.strip().split("\n"))
        return inner + "\n\n"
    if name in ("ul", "ol"):
        lines = []
        ordered = name == "ol"
        idx = 1
        for li in node.find_all("li", recursive=False):
            li_inner = render_children(li)
            marker = "{}. ".format(idx) if ordered else "- "
            for i, l in enumerate(li_inner.strip().split("\n")):
                if i == 0:
                    lines.append(marker + l.strip())
                else:
                    lines.append("  " + l.strip())
            idx += 1
        return "\n".join(lines) + "\n\n"
    if name == "hr":
        return "\n---\n\n"
    if name == "table":
        # 普通表格（非 highlight）简单转置
        rows = []
        for tr in node.find_all("tr"):
            cells = [render_inline(td).replace("\n", " ") for td in tr.find_all(["td", "th"])]
            rows.append("| " + " | ".join(cells) + " |")
        if rows:
            return "\n".join(rows) + "\n\n"
        return ""
    if name == "div" or name == "section":
        return render_children(node)
    if name == "iframe":
        src = node.get("src", "")
        return "<iframe src=\"{}\"></iframe>\n\n".format(src) if src else ""
    # 其它：按行内元素处理（保留链接、加粗、more 锚点等）
    return inline_to_md(node) + "\n\n"


def render_children(node):
    parts = []
    for child in node.contents:
        if isinstance(child, str):
            t = child.strip()
            if t:
                parts.append(t + "\n\n")
            continue
        parts.append(render_block(child))
    return "".join(parts)


def collect_posts():
    posts = []
    for path in sorted(glob.glob(os.path.join(ROOT, "year", "**", "index.html"), recursive=True)):
        try:
            posts.append((path, parse_post(path)))
        except Exception as e:
            print("PARSE ERROR {}: {}".format(path, e), file=sys.stderr)
    return posts


def slug_for(title):
    s = re.sub(r"[\\/:*?\"<>|\s]+", "-", title)
    s = s.strip("-")
    return s or "untitled"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan", action="store_true")
    ap.add_argument("--out", type=str)
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    posts = collect_posts()
    print("TOTAL:", len(posts))
    for path, p in posts:
        body_len = len(p["body"].get_text(strip=True)) if p["body"] else 0
        print("{}\ttitle={}\tdate={}\tcats={}\ttags={}\tbody={}chars".format(
            os.path.relpath(path, ROOT), p["title"], p["date"],
            "/".join(p["categories"]), "/".join(p["tags"]), body_len))
    if args.scan or not args.out:
        return

    os.makedirs(args.out, exist_ok=True)
    for path, p in posts:
        fm = ["---"]
        fm.append("title: {}".format(p["title"]))
        if p["date"]:
            d = p["date"].replace("Z", "+00:00")
            fm.append("date: {}".format(d))
        if p["updated"]:
            u = p["updated"].replace("Z", "+00:00")
            fm.append("updated: {}".format(u))
        if p["tags"]:
            fm.append("tags:")
            for t in p["tags"]:
                fm.append("  - {}".format(t))
        if p["categories"]:
            fm.append("categories:")
            for c in p["categories"]:
                fm.append("  - {}".format(c))
        fm.append("---")
        md_body = render_children(p["body"]) if p["body"] else ""
        content = "\n".join(fm) + "\n\n" + md_body.strip() + "\n"
        slug = slug_for(p["title"])
        out_path = os.path.join(args.out, slug + ".md")
        # 文件名冲突：加序号，除非显式 --overwrite
        n = 1
        while os.path.exists(out_path) and not args.overwrite:
            out_path = os.path.join(args.out, "{}-{}.md".format(slug, n))
            n += 1
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("WROTE", out_path)


if __name__ == "__main__":
    main()
