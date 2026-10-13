---
title: Hexo 添加 SEO
date: 2017-12-19T11:12:47+08:00
updated: 2019-05-20T12:41:14+08:00
tags:
  - Hexo
categories:
  - Hexo
---

- 站内地图
  
  
  
  
  站点地图是一种文件，您可以通过该文件列出您网站上的网页，从而将您网站内容的组织架构告知Google和其他搜索引擎。Googlebot等搜索引擎网页抓取工具会读取此文件，以便更加智能地抓取您的网站



<!-- more -->



- 安装插件

```bash
npm install hexo-generator-sitemap --save
npm install hexo-generator-baidu-sitemap --save
```

- _config.yml添加如下配置

```js
# 自动生成sitemap
sitemap:
path: sitemap.xml
baidusitemap:
baidu_path: baidusitemap.xml
```

- 修改 node_modules\hexo-generator-baidu-sitemap\baidusitemap.ejs
  文件，将url换成自己的地址
- 修改 node_modules\hexo-generator-sitemap\sitemap.xml文件，将url换成自己的地址
- 编译blog

```bash
hexo g
```

博客public目录生成sitemap.xml以及baidusitemap.xml就表示成功了。
