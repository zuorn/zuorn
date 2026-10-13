---
title: Hammerspoon - 岂止于窗口管理
date: 2019-07-06T14:58:30+08:00
updated: 2020-07-05T13:29:36+08:00
tags:
  - 工具
categories:
  - 工具
---

> 为什么要费尽心思的用键盘替代鼠标操作。

在使用电脑的过程中，最优先的操作方式应该是**键盘**，而次等的方式才是鼠标，因为鼠标需要使用者在键盘和鼠标之间来回切换，因此影响效率。而 **“纯键盘操作”** 需要使用者记忆大量的键位和操作模式，所以**纯键盘**从来都是高阶操作。

鼠标长久以来都是顺应人的本能去设计的。但高阶操作是什么？高阶操作就是训练人克服本能，用**更有效**、**更科学**的但**非本能**的方式去应对，所以才需要大量的练习，大量的实战，从而形成[肌肉记忆](https://baike.baidu.com/item/%E8%82%8C%E8%82%89%E8%AE%B0%E5%BF%86)和[思维定势](https://baike.baidu.com/item/%E6%80%9D%E7%BB%B4%E5%AE%9A%E5%8A%BF?fromtitle=%E6%80%9D%E7%BB%B4%E6%83%AF%E6%80%A7&fromid=3457840)去对抗本能。vim 如此,Hammerspoon 也如此。

有些了解过 Hammerspoon 可能把它看作一款窗口管理工具，用此来替代 Magent 等付费工具，但 Hammerspoon 的玩法绝不仅于此，本文将介绍 Hammerspoon 及我的配置。



<!-- more -->



### Hammerspoon介绍

> [Hammerspoon](http://www.hammerspoon.org/) 是一款**免费开源**的 app，通过桥接操作系统与 Lua 脚本引擎的方式，让我们可以通过编写 [Lua](http://www.lua.org/docs.html) 代码来实现操作应用程序、窗口、鼠标、文本、音频设备、电池、屏幕、剪切板、定位、wifi等。基本囊括了系统的各方面。

### 安装

- 通过 Homebrew 安装：
  （如果不了解 `Homebrew` 看[这里](https://zuorn.top/year/05/22/homebrew-yuan/)。）
  
  ```plain
  brew cask install hammerspoon
  ```
- 手动下载安装：[https://github.com/Hammerspoon/hammerspoon/releases/tag/0.9.75](https://github.com/Hammerspoon/hammerspoon/releases/tag/0.9.75) 然后将应用程序拖到`/Applications/`。

![](http://ww4.sinaimg.cn/large/006tNc79ly1g4q4yawr88j30ee0bydgm.jpg)

第一次打开需要授予辅助功能权限，点击 `Enable Accessibility`即可。此时在 `~/.hammerspoon/init.lua` 写入自己的配置文件在 Hammerspoon 单栏图标并选择 `Reload Config` 重载配置即可生效。

## 配置与升级:

将配置文件克隆到本地根目录。

```plain
git clone https://github.com/zuorn/hammerspoon_config ~/.hammerspoon
```

重新加载配置文件即可生效。

如果提示：already exists and is not an empty directory.
先删除目录

```plain
rm -rf ~/.hammerspoon
```

升级：

```plain
cd ~/.hammerspoon && git pull
```

## 功能实现

> 本配置基于 vim 风格，实现了窗口管理，剪切板，倒计时，快速启动等功能。所有模式按照指定快捷键进入，所有模式都可以用 `esc` 或 `q`退出。在进入对应模式之前只有模式快捷键生效，进入对应模式之后此模式的操作快捷键生效。

可以按下快捷键 `shift` + `option` + `/` 显示帮助面板查看各个模式快捷键。再按照提示切换模式。

![](http://ww3.sinaimg.cn/large/006tNc79ly1g4q4xvmcbvj316o0i00ul.jpg)

### 窗口管理

按下前缀键 `Option` + `R` 进入窗口管理模式：

- 使用 `h、j、k、l` 移动为上下左右的半屏
- 使用 `y、u、i、o`（即 hjkl 上方按键）移动为左上/左下/右上/右下的四分之一窗口
- 使用 `c` 居中，按下 `=、-` 进行窗口大小缩放
- 使用 `w、s、a、d` 向上下左右移动窗口
- 使用 `H、J、K、L` 向左/下增减窗口大小
- 使用方向键 `上、下、左、右` 移动到相应方向上的显示器（多块显示器的话）
- 使用 `[,]` 左三分之二屏和右三分之二屏
- 使用 `空格` 将窗口投送到另外一块屏幕（假如有两块以上显示器的话）
- 使用 `t` 光标移动到所在窗口的中间位置
- 使用 `tab` 显示帮助面板，查看键位图
- 使用 q 或 Esc 退出管理
  
  ![](http://ww4.sinaimg.cn/large/006tNc79ly1g4pz9dhogwj31c00u04aw.jpg)

### 应用快速切换

按下前缀键 `Option` + `tab` 显示窗口提示，按下对应应用显示的字母快速切换。
![](http://ww1.sinaimg.cn/large/006tNc79ly1g4q4x5cxatj31z40u0k5e.jpg)

### 展示应用快捷键

按下快捷键 `Option` + `s` 展示当前应用快捷键。

![](http://ww2.sinaimg.cn/large/006tNc79ly1g4q4wsyk6lj31z40u0n5i.jpg)

### 快速启动

按下快捷键 `Option` + `a` 打开快速启动，按下对应字母快速打开应用。

![](http://ww1.sinaimg.cn/large/006tNc79ly1g4q4w5a6e8j31z40u0gvs.jpg)

### AClock - 显示当前时间

按下 `Option` + `t` 显示当前时间。

![](http://ww4.sinaimg.cn/large/006tNc79ly1g4q4utqg63j31z40u0tng.jpg)

### 倒计时（番茄钟）

按下 `Option` + `i` 打开倒计时面板，按下对应数字开始计时。

![](http://ww1.sinaimg.cn/large/006tNc79ly1g4q4w5a6e8j31z40u0gvs.jpg)

### 系统剪切板

按下 `Option` + `c` 打开剪切板面板。

![](http://ww4.sinaimg.cn/large/006tNc79ly1g4q4u4g2jgj31z40u0gvb.jpg)

功能：

- 保存会话
- 恢复上一个会话
- 在浏览器中打开
- 使用百度搜索
- 使用谷歌搜索
- 保存到桌面
- 使用 github 搜索
- 在 Sublime Text 打开

### 顶部菜单栏实时显示网速

没有对应快捷键，默认开启。

![](http://ww2.sinaimg.cn/large/006tNc79ly1g4q4tni77ej30ks0a2myp.jpg)

### 其他快捷键

- 粘贴 chrome 或 safari 打开最前置的网址：
  
  `option`
  
  +
  
  `v`
- 显示 Hammerspoon 控制台：
  
  `option`
  
  +
  
  `v`
- 锁定电脑快捷键：
  
  `option`
  
  +
  
  `l`
- 重新加载配置文件：
  
  `cmd`
  
  +
  
  `shift`
  
  +
  
  `ctrl`
  
  +
  
  `r`
- 临时禁用所有快捷键(注意：只能手动接禁。)：
  
  `cmd`
  
  +
  
  `shift`
  
  +
  
  `ctrl`
  
  +
  
  `q`

## 自定义配置

拷贝私有配置文件

```plain
cp ~/.hammerspoon/config-example.lua ~/.hammerspoon/private/config.lua
```

按照注释编辑私有配置文件 `~/.hammerspoon/private/config.lua` 即可。

## 其他功能（后续实现）

- 按下前缀键滚动鼠标滚轮调节系统音量
- 添加鼠标模式，进入鼠标模式后按下对应按键实现鼠标所有按键。
- 切换 wifi 提醒
- 显示已安装卷的列表以及桌面上每个指示可用空间的饼图
- 连接/断开耳机时播放/暂停音乐播放器
- 添加音乐控制模式，进入后通过按键控制 网易云音乐 和 iTunes

#### 可自定义范围：

- 指定要启用模块
  
  找到配置文件启用模块，注释对应模块可禁止用对应功能。
- 绑定快速启动 app 及快捷键
- 自定义模式快捷键
- 自定义 hammerspoon 快捷键绑定

## 自己写配置

Lua 是一种非常简单的语言，没有编程经验也很容易上手。hammerspoon 官方也提供了一份[教程](http://www.hammerspoon.org/go/)，或者看看[菜鸟教程](https://www.runoob.com/lua/lua-tutorial.html)。

官方还有很多现成的 [Spoons 勺子？](https://www.hammerspoon.org/Spoons/) 可以用，有些直接拿来绑定一下键位就可以直接用了，如果觉得官方勺子不符合自己的需求，你也可以把它改成自己想要的样子。多看看官方文档和相关的文章，以及官方勺子的源码，就很容易定制一个属于自己独一无二的神器。

## 参考：

- [Hammerspoon Spoons](https://www.hammerspoon.org/Spoons/)
- [awesome-hammerspoon](https://github.com/ashfinal/awesome-hammerspoon)
