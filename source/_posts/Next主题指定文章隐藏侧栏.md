---
title: Next主题指定文章隐藏侧栏
date: 2019-01-22T23:32:57+08:00
updated: 2019-05-20T12:41:14+08:00
tags:
  - Hexo
---

#### 缘由

可能你需要加一个单独的页面，比如about页面，希望隐藏next主题的侧栏，那么请看下去。



<!-- more -->



#### 修改

根据[issues-943](https://github.com/iissnan/hexo-theme-next/issues/943)找到了my-project/themes/next/layout/_marcro/sidebar.swig中找到下一列信息。

```js
{% set display_toc = is_post and theme.toc.enable or is_page and theme.toc.enable %}
```

修改为：

```js
{% set display_toc = is_post and theme.toc.enable and !page.no_toc or is_page and theme.toc.enable and !page.no_toc %}
```

这样你就可以在不想要显示目录的文章头部加一行：`no_toc: true`即可。
