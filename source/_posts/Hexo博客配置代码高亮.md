---
title: Hexo博客配置代码高亮
date: 2017-09-10T00:30:55+08:00
updated: 2019-05-20T12:41:14+08:00
tags:
  - Hexo
categories:
  - Hexo
---

#### 博客根目录安装

```bash
npm i -S hexo-prism-plugin --save
```

#### 编辑/_config.yml(默认true改成false)：



<!-- more -->



```bash
highlight：
   enable：false
``` 


#### 编辑/_config.yml添加以下内容：

```bash
prism_plugin:
  mode: 'preprocess'    # realtime/preprocess
  theme: 'default'
  line_number: false    # default false
```
