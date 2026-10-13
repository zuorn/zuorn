---
title: Hexo常用命令
date: 2017-09-08T14:54:19+08:00
updated: 2019-05-20T12:41:15+08:00
tags:
  - Hexo
categories:
  - Hexo
---

### Hexo

```bash
npm install hexo -g #安装
npm update hexo -g #更新
hexo init #初始化
```



<!-- more -->



### 草稿

```bash
hexo publish [layout] <title> #发表草稿。
```

### 写作

```bash
hexo n "name" #新建文章
hexo g #生成静态网页
hexo p #发表草稿。
hexo s #启动服务
hexo d #部署网站 参数：-g 部署之前先生成静态文件。
```

# 服务器

Hexo 3.0 把服务器独立成了个别模块，您必须先安装才能使用。

```bash
npm install hexo-server --save #安装服务
    
hexo s #启动服务
hexo server -p 5000 #更改端口
hexo s -s #静态模式
hexo s -i 192.168.1.1 #自定义ip
    
hexo clean #清除缓存
```

# 部署

```text
hexo d -g
hexo g -d
```

两者作用完全相同。
