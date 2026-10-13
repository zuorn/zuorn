---
title: Markdown入门
date: 2017-09-08T10:03:55+08:00
updated: 2019-05-20T12:41:15+08:00
tags:
  - Markdown
categories:
  - 工具
---

> [Markdown](https://zh.wikipedia.org/wiki/Markdown)是一种[轻量级标记语言](https://zh.wikipedia.org/wiki/%E8%BD%BB%E9%87%8F%E7%BA%A7%E6%A0%87%E8%AE%B0%E8%AF%AD%E8%A8%80)，它的优点在于易于阅读、易于撰写的纯文字格式， 并且可以自由转换成多种格式。目前也被越来越多的写作爱好者，撰稿者广泛使用。



<!-- more -->



### 介绍

Markdown旨在尽可能容易阅读和易于写入。

然而，可读性首先被强调。标记格式的文档应该按照原样发布，而不是像标签或格式化说明一样标记。虽然Markdown的语法受到几个现有的文本到HTML过滤器的影响，包括Setext，atx，Textile，reStructuredText， Grutatext和EtText - Markdown语法的最大灵感来源是纯文本电子邮件的格式。

为此，Markdown的语法完全由标点符号组成，标点符号被仔细选择，看起来就像它们的意思。例如，一个字上的星号实际上看起来像*强调*。标记列表看起来好像列表。

### 语法：

Markdown作为一种轻量级标记语言，它的语法简洁明了、学习起来容易。

参考：
[官方说明](https://daringfireball.net/projects/markdown/syntax)
[Markdown 中文版语法说明 ](http://wowubuntu.com/markdown/#list)

#### 标题

```text
# 第一级标题
## 第二级标题
###### 第六级标题
```

效果如下：

# 第一级标题

## 第二级标题

###### 第六级标题

## 强调

```js
*这些文字会生成*
_这些文字会生成`_

**这些文字会生成**
__这些文字会生成`__
```

效果如下：

*这些文字会生成*
*这些文字会生成`*

**这些文字会生成**
**这些文字会生成`**

## 列表

### 无序列表

```js
* 列表一
* 列表二
* 列表三
```

效果：

- 列表一
- 列表二
- 列表三

### 有序列表

```js
1. 列表一
2. 列表二
3. 列表三
```

效果如下：

1. 列表一
2. 列表二
3. 列表三

### 任务列表（Task lists）

```js
- [ ] 任务一 未做任务
- [x] 任务二 已做任务
```

效果如下：

- 任务一 未做任务
- 任务二 已做任务

## 图片

```js
![图片名称](地址)
```

#### 链接

```js
[名称](链接地址)
```

## 区块引用

```js
某某说:
> balabala
```

效果：
某某说:

> balabala

## 行内代码

```js
`代码`
```

效果如下：
`代码`

## 多行或者一段代码

```js
代码段
```

效果如下：

```js
代码段
```

## 顺序图或流程图

```text
123张三->李四: 嘿，小四儿, 你妈喊你回家吃饭呢！Note right of 李四: 李四愣了一下，说：李四-->张三: 哦，知道啦！

12345678st=>start: 开始e=>end: 结束op=>operation: 我的操作cond=>condition: 确认？st->op->condcond(yes)->econd(no)->op
```

效果：

```plain
张三->李四: 嘿，小四儿, 你妈喊你回家吃饭呢！
Note right of 李四: 李四愣了一下，说：
李四-->张三: 哦，知道啦！
```

#### 表格

Markdown 语法：

```js
表头一 | 表头二
--------- | -------------
第一列第一格 | 格第二列第一格
第一列第二格 | 格第二列第二格
```

效果如下：

| 表头一 | 表头二 |
| 第一列第一格 | 格第二列第一格 |
| 第一列第二格 | 格第二列第二格 |

#### 删除线

```js
~~删除这些~~
```

效果如下：

删除这些

#### 分隔线

以下三种方式都可以生成分隔线：

```js
***

*****

- - -
```

效果如下：


---


---


---

#### 脚注（Footnote）

```js
这是一个脚注：[^sample_footnote]
```

效果如下：

这是一个脚注：[^sample_footnote](这里是脚注信息)

## 工具：

常见的Markdown工具有[Ulysses](https://ulyssesapp.com/)，[Mou](http://25.io/mou/)，[Sublime Text 3](http://www.sublimetext.com/3)等等。

个人比较喜欢[mweb](https://itunes.apple.com/cn/app/mweb-%E4%B8%93%E4%B8%9A%E7%9A%84markdown%E5%86%99%E4%BD%9C-%E8%AE%B0%E7%AC%94%E8%AE%B0-%E9%9D%99%E6%80%81%E5%8D%9A%E5%AE%A2%E7%94%9F%E6%88%90%E8%BD%AF%E4%BB%B6/id954188948?mt=12)，几乎所有的语法都有对应的快捷键，而且还能一键生成&上传至博客。

具体使用方法见[官方文档](http://zh.mweb.im/help.html)。

另外还有一个[免费版的](https://itunes.apple.com/cn/app/mweb-lite-%E4%B8%93%E4%B8%9A%E7%9A%84markdown%E5%86%99%E4%BD%9C%E8%BD%AF%E4%BB%B6/id979033429?mt=12)，
![](http://ovlnt0xy1.bkt.clouddn.com/mweb.png)
