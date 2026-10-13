---
title: cvim
date: 2017-09-09T23:18:44+08:00
updated: 2019-05-20T12:41:15+08:00
tags:
  - 工具
categories:
  - 工具
---

> 当我在填写网页内容的时候，我的手不得不从鼠标和键盘上来回切换，于是我开始寻找解决这个问题的办法，[cvim](https://chrome.google.com/webstore/detail/cvim/ihlenndgcmojhcghmfjfneahoeklbjjh)很好的解决了这个问题。



<!-- more -->



### 什么是[cvim](https://chrome.google.com/webstore/detail/cvim/ihlenndgcmojhcghmfjfneahoeklbjjh)？

cvim适用于[Google Chrome](https://www.google.com/chrome/index.html)的[Vim](https://vim.sourceforge.io/download.php)。

#### 作者的话：

> 我讨厌使用鼠标，尤其是在学习Vim之后。使用我的桌面（Linux），我有很多键绑定，使事情变得更容易：我用Alt + w打开Chrome，我用Alt + Shift + d关闭一个窗口，我打开一个Alt + t的终端。这对Chrome很难处理，因为它没有自定义键盘快捷键的部分，但仍然需要使用鼠标来执行点击链接。 cVim旨在尽可能地消除此问题，Chrome扩展API将允许它。

### cvim的优势是什么？

- 支持自定义搜索引擎
- 支持插入符/Visual模式 （！！超赞有木有！！）
- 支持正则表达式！！
- 命令支持tab补全！
- 支持自定义键映射！！（也就是你可以自己写vimrc，这才是完整的vim好不好！！可以备份到github）
- 自定义命令

### 如何获取cvim

[chrome web sotre](https://chrome.google.com/webstore/category/extensions)搜索[cvim](https://chrome.google.com/webstore/detail/cvim/ihlenndgcmojhcghmfjfneahoeklbjjh)安装即可，或者点击本文[cvim](https://chrome.google.com/webstore/detail/cvim/ihlenndgcmojhcghmfjfneahoeklbjjh)直接安装。

### cvim用法：

我这里分别从正常模式、链接提示、标签栏导航、视觉／插入模式、命令模式说明。

#### 正常模式：

- j， s 向下滚动
- k， w 向上滑动
- h 向左滚动
- l 向右滚动
- d 滚动一半页面
- u， e 滚动一半页面
- gg 滚动到页面顶部
- G 滚动到页面的底部
- gi 转到第一个输入框
- gI 转到最后一个输入框

#### 链接提示：

- f 打开当前选项卡中的链接
- F 在新标签页中打开链接
- W 在新窗口中打开链接
- A 重复最后提示命令
- q 触发悬停事件
- Q 触发不起眼的事件
- mf 打开多个链接
- gy 从链接复制URL到剪贴板
- yy 将当前页面的URL复制到剪贴板
- yY 将当前帧的URL复制到剪贴板

#### 其他：

- : 打开命令栏
- / 打开搜索栏
- ? 打开搜索栏（反向搜索）
- I 搜索浏览器历史记录
- zr 重新启动Google Chrome
- i 进入插入模式
- r 重新加载当前选项卡（刷新）
- gR 重新加载当前选项卡+本地缓存
- z
  
  切换图像缩放（与仅在图像页面上单击图像相同）
- yh 从查找模式复制当前匹配的文本（如果有）
- b 搜寻书签(相当于命令:bookmarks）
- p 打开剪贴板选择
- gj 隐藏下载栏
- gq 停止加载当前选项卡
- gQ 停止加载所有标签

#### 标签导航：

- gt，K，R 导航到下一个选项卡
- gT，J，E 导航到上一个选项卡
- g0， g$ 转到第一个/最后一个选项卡
- x 关闭当前选项卡
- X 打开最后关闭的标签页
- H， S 返回上一个标签
- L， D 前进下一个标签
- B 搜索另一个活动选项卡
- < 向左移动当前标签
- > 向右移动当前标签
- 查找模式(/进入）：
- n 下一个搜索结果
- N 以前的搜索结果
- v 进入视觉/插入模式（突出显示当前搜索/选择）
- V 从插入模式/当前突出显示的搜索进入视线模式

#### 视觉／插入模式（i插入、v视觉）：

- 将视觉模式退出插入模式/退出插入模式到正常模式
- v 在视觉/插入模式之间切换
- h，j，k，l 移动插入位置/扩展视觉选择
- y 配合当前的选择
- n 选择下一个搜索结果
- N 选择先前的搜索结果
- p 打开当前选项卡中的突出显示
- P 在新标签中打开突出显示的文本

#### 命令模式(:打开命令栏）：

- . 重复最后一个命令
- :new url 打开一个新窗口
- :bookmarks url  从书签中打开一条新的标签
- :open url 打开一个新标签
- :history url 打开一条历史标签
- :quit 关闭当前标签
- :qall 关闭当前窗口（注意：是关闭当前的窗口，不是关闭标签)
