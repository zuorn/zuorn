---
title: hexo速度优化，gulp压缩静态资源
date: 2019-01-25T00:28:01+08:00
updated: 2020-07-05T13:35:11+08:00
tags:
  - hexo
categories:
  - Hexo
---

> hexo生成的的public文件夹里的源文件有很多空白，这些空白占据一定空间。[gulp](https://www.gulpjs.com.cn/)可以高效的压缩这些静态资源，从而提高访问速度。



<!-- more -->



#### 插件安装

安装`gulp`工具

```js
npm install gulp
```

安装gulp模块：

```text
gulp-htmlclean // 清理html
gulp-htmlmin // 压缩html
gulp-minify-css // 压缩css
gulp-uglify // 混淆js
```

安装命令：

```js
npm install gulp-htmlclean gulp-htmlmin gulp-minify-css gulp-uglify --save
```

#### 创建任务

在站点根目录下新建`gulpfile.js`文件，内容如下：

```js
var gulp = require('gulp');

//Plugins模块获取
var minifycss = require('gulp-minify-css');
var uglify = require('gulp-uglify');
var htmlmin = require('gulp-htmlmin');
var htmlclean = require('gulp-htmlclean');
//压缩css
gulp.task('minify-css', function () {
return gulp.src('./public/**/*.css')
.pipe(minifycss())
.pipe(gulp.dest('./public'));
});
//压缩html
gulp.task('minify-html', function () {
return gulp.src('./public/**/*.html')
.pipe(htmlclean())
.pipe(htmlmin({
removeComments: true,
minifyJS: true,
minifyCSS: true,
minifyURLs: true,
}))

.pipe(gulp.dest('./public'))
});
//压缩js 不压缩min.js
gulp.task('minify-js', function () {
return gulp.src(['./public/**/*.js', '!./public/**/*.min.js'])
.pipe(uglify())
.pipe(gulp.dest('./public'));
});

//4.0以前的写法 
//gulp.task('default', [
  //  'minify-html', 'minify-css', 'minify-js'
//]);
//4.0以后的写法
// 执行 gulp 命令时执行的任务
gulp.task('default', gulp.parallel('minify-html', 'minify-css', 'minify-js', function() {
  // Do something after a, b, and c are finished.
}));
```

#### 使用

命令：

```js
hexo clean //先清理文件
hexo g  //编译生成静态文件
gulp  //gulp插件执行压缩任务
hexo s //开启服务
```

当然，通过一个命令也可以：

```js
hexo g && gulp -d
```
