---
title: Next主题自动更换背景
date: 2018-10-06T01:31:04+08:00
updated: 2020-07-05T13:35:53+08:00
tags:
  - hexo
categories:
  - Hexo
---

> 如果觉得next的空白主题看腻了或者太多人用觉得不够个性化，那么不妨试试自动更新背景图片。



<!-- more -->



## 图片来源

自动更换背景的实现是修改添加背景的css样式实现。图片来源是

[https://source.unsplash.com/](https://source.unsplash.com/)

这个网站，里面不仅免费提供了很多高清美图，而且还提供api接口调用，实在是良心。这里实现的原理也是调用了这个网站的接口。

## 修改背景样式

修改`themes\next\source\css\_custom\custom.styl`文件，这个是Next故意留给用户自己个性化定制一些样式的文件，添加以下代码：

```js
body {

    background:url(https://source.unsplash.com/random/1600x900);

    background-repeat: no-repeat;

    background-attachment:fixed;

    background-position:50% 50%;

}
```

如果自己不喜欢这个网址提供的图片做背景，那么修改url()里面的路径即可。repeat、attachment、position就是调整图片的位置，不重复出现、不滚动等等。

## 修改不透明度

完成这一步其实背景就会自动更换了，但是会出现一个问题，因为next主题的背景是纯透明的，这样子就造成背景图片的影响看不见文字，这对于博客来说肯定不行。

那么就需要调整背景的不透明度了。同样是修改t`hemes\next\source\css _custom\custom.styl`文件。在后面添加如下代码：

```js
.main-inner { 

    margin-top: 60px;

    padding: 60px 60px 60px 60px;

    background: #fff;

	opacity: 0.8;

    min-height: 500px;

}
```

```text
* background: #fff; 白色
* opacity: 0.8;不透明度
```

## 效果：

![](https://blog-1256335675.cos.ap-chengdu.myqcloud.com/2019-06-18-006tNbRwgy1fvxvc6azb4j31kw0vknpd.jpg)
