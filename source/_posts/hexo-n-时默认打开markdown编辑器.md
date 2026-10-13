---
title: hexo n 时默认打开markdown编辑器
date: 2018-04-10T17:11:28+08:00
updated: 2019-06-19T00:49:00+08:00
tags:
  - Hexo
categories:
  - Hexo
---

![](https://blog-1256335675.cos.ap-chengdu.myqcloud.com/2019-06-18-006tKfTcgy1fqa9b4cyrwj30m608mq3g.jpg)



<!-- more -->



首先：

> - 在Hexo目录下的
>   
>   `scripts`
>   
>   目录中创建一个
>   
>   `JavaScript`
>   
>   脚本文件。

- 如果没有这个
  
  `scripts`
  
  目录，则新建一个。
- `scripts`
  
  目录新建的
  
  `JavaScript`
  
  脚本文件可以任意取名。

通过这个脚本，我们用其来监听hexo new这个动作，并在检测到hexo new之后，执行编辑器打开的命令。

windows平台的Hexo用户，则将下列内容写入你的脚本：

```js
var spawn = require('child_process').exec;

// Hexo 2.x 用户复制这段
hexo.on('new', function(path){
  spawn('start  "markdown编辑器绝对路径.exe" ' + path);
});

// Hexo 3 用户复制这段
hexo.on('new', function(data){
  spawn('start  "markdown编辑器绝对路径.exe" ' + data.path);
});
```

Mac平台Hexo用户，则将下列内容写入你的脚本：

```js
var exec = require('child_process').exec;

// Hexo 2.x 用户复制这段
hexo.on('new', function(path){
    exec('open -a "markdown编辑器绝对路径.app" ' + path);
});
// Hexo 3 用户复制这段
hexo.on('new', function(data){
    exec('open -a "markdown编辑器绝对路径.app" ' + data.path);
});
```

保存并退出脚本之后，在命令行中键入：

```js
hexo new "auto open editor test"
```

就可以顺利打开自动生成的md文件了。

原文转自：[这里～](https://notes.wanghao.work/2015-06-29-Hexo%E6%B7%BB%E5%8A%A0%E6%96%87%E7%AB%A0%E6%97%B6%E8%87%AA%E5%8A%A8%E6%89%93%E5%BC%80%E7%BC%96%E8%BE%91%E5%99%A8.html)
