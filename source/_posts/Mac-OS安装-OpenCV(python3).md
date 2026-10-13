---
title: Mac OS安装 OpenCV(python3)
date: 2018-01-03T00:45:56+08:00
updated: 2019-05-20T12:41:15+08:00
tags:
  - python
categories:
  - 技术
---

运行命令：

```sh
brew install opencv3 --with-python3 --c++11 --with-contrib  
brew link --force opencv3
```



<!-- more -->



测试：

```python
$ python3  
Python 3.5.1 (default, May 20 2016, 12:52:19)  
[GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin  
Type "help", "copyright", "credits" or "license" for more information.  
>>> import cv2
```

如果没有报错，说明安装成功了，恭喜你！先解释一下上面的命令
brew install opencv3 这条命令用来指明安装python3版本的，（有opencv ，opencv3两种python版本，前一种对应python2），
–with-python3用来告诉homebrew用来让opencv支持python3，

–c++11 用来告诉homebrew提供c++11支持，
–with-contrib 用来安装opencv的contrib支持。

如果上面的步骤进行之后，还是没有安装成功opencv（其实opencv已经安装了，只是没有正确的和python3关联起来），可以重新试一下下面的命令：

```sh
brew unlink opencv3 && brew link --force opencv3
```

再次试一下是否成功，如果成功了，恭喜你不用再往下面看了，如果没有成功，接着看，我们下面的任务就是正确地使python3和opencv关联起来。注意到我们上面使用homebrew安装了程序，homebrew安装的程序位置都在 下面。

```js
/usr/local/Cellar/
```

所以我们需要找到的就是opencv的cv2*.so文件，（参考我前面ubuntu安装opencv最后也是关联cv2.so文件），最终我的so文件位置为：

```js
/usr/local/Cellar/opencv3/3.1.0_4/lib/python3.5/site-packages/cv2.cpython-35m-darwin.so
```

下面就是和python3环境关联，还有和虚拟virtualenv开发环境关联。
我关联的是虚拟环境，python实体环境也是同理，只要转到python3 的site-packages文件夹下面和原来上面的so建立一个软链接就行。

```js
cd /usr/local/lib/python3.5/site-packages  
ln -s /usr/local/Cellar/opencv3/3.1.0_4/lib/python3.5/site-packages/cv2.cpython-35m-darwin.so cv2.so
```

激活virtualenv虚拟环境，输入python

```python
>>> import cv2  
>>> cv2.__version__  
'3.1.0'
```

运行以下命令，则说明安装成功。

参考：[戳这里](https://gravityjack.com/news/opencv-python-3-homebrew/)
