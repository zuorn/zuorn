---
title: Mac OS 下 Sublime Text 3 运行Java
date: 2019-01-12T01:01:53+08:00
updated: 2020-07-05T13:30:32+08:00
tags:
  - 工具
categories:
  - 工具
---

.



<!-- more -->



#### 在Sublime中安装Package Resource Viewer，具体操作步骤如下：

```text
* ctrl+shift+p打开package control； 
* 输入Install Package； 
* 搜索Package Resource Viewer并安装。
```

#### 修改Javac.sublime-build：

```text
安装Package Resource Viewer就是为这一步服务。同上面的步骤，打开package control，输入PackageResourceViewer:Open Resource，回车后输入java，回车后输入Javac.sublime-build,就能够打开我们所需要修改的文件：Google 了下，找到了两种配置文件。
```

```shell
{

"shell_cmd": "javac -encoding utf-8 $file_name && java $file_base_name",

"file_regex": "^ *\\[javac\\] (.+):([0-9]+):() (.*)$",

"selector": "source.java",

"encoding": "utf-8"

}
```

```shell
{

"cmd": ["javac \"$file_name\" && java \"$file_base_name\""],

"working_dir": "${project_path:${folder}}",

"file_regex": "^(...*?):([0-9]*):?([0-9]*)",

"selector": "source.java",

"shell": true,

"encoding": "utf-8"

}
```

#### 选择Build System，选择上一步保存的配置文件

![](https://blog-1256335675.cos.ap-chengdu.myqcloud.com/2019-06-18-su.jpg)

#### Command+B编译运行

```text
运行的时候会在桌面上生成一个　.class文件，可以通过配置文件将生成的.class文件删除。
```

```shell
"shell_cmd": "javac -encoding utf-8 $file_name && java $file_base_name && rm -rf $file_base_name.class"
```
