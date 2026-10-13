---
title: macOS 轻松愉快的解压 rar 压缩包
date: 2019-06-28T20:13:21+08:00
updated: 2020-07-05T13:29:32+08:00
tags:
  - 工具
categories:
  - 工具
---

macOS 自带的压缩软件不支持 rar 格式的文件解压缩，于是需要找一个第三方压缩软件。Keka 一个不错的软件，但是它默认的压缩文件图标也太丑了吧。而且我对解压缩并那么多的需求，在用了一段时间之后发现了 unrar 就果断放弃了。



<!-- more -->



## 安装

使用 homebrew 安装

```plain
brew install unrar
```

## 用法：

```plain
unrar 参数 压缩文件名 路径
```

解压参数：

```plain
e             解压压缩文件到当前目录
x             用绝对路径解压文件
```
