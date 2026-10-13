---
title: 使用ADB无线连接Android真机进行调试
date: 2018-01-05T09:55:21+08:00
updated: 2019-06-19T00:50:29+08:00
tags:
  - 调试
categories:
  - 技术
---

![](https://blog-1256335675.cos.ap-chengdu.myqcloud.com/2019-06-18-006tKfTcgy1fqa8x1kfm7j30gi08n74m.jpg)



<!-- more -->



## 什么是 ADB?

Android调试桥（ adb ）是一个开发工具，帮助安卓设备和个人计算机之间的通信。 这种通信大多是在USB电缆下进行，但是也支持Wi-Fi连接。 adb 还可被用来与电脑上运行的安卓模拟器交流通信。 adb 对于安卓开发来说就像一把“瑞士军刀”。

## 通过 Homebrew 安装

```js
brew cask install android-platform-tools
```

测试是否安装正常

```js
adb devices
```

## 前提条件

- 手机和电脑处于同一个局域网内
- 电脑上已经安装好ADB工具

## 步骤

### 1、打开手机

让手机在指定的端口可以接收到TCP/IP连接。

1. 确保手机开启了usb调试
2. 用usb线把手机和电脑连接起来
3. 执行命令：adb tcpip 5555

执行成功后就可以把usb线拔掉了，端口可以不是5555，这个官方默认使用的。

### 2、找到手机的的IP地址

执行命令

```js
adb connect 192.168.1.100:5555
```

如果提示：

> connected to 192.160.1.100:5555

则表示连接成功，如果端口号是5555可以省略，直接：

```js
db connect 192.168.1.100
```

### 如果没有连接成功

如果确定你的网络和端口都没问题，可以尝试重启一下adb服务：

> adb kill-server

然后再进行连接，实在还是不行就Google吧。

### 连接成功

如果连接成功的话，执行以下命令查看当前连接的设备列表：

```js
adb devices
```

可以看到连接的设备，像这样

> $ adb devices
> List of devices attached
> 192.168.1.100:5555 device

以后没有数据线也可以调试手机或者在上面运行自动化测试了。

## 注意事项

1. 更换一个网络环境需要使用新IP重新connect即可。
2. 但是如果手机重启了，就需要重新连接数据线再次开启端口。
3. 开启端口可以通过adb，也可以直接在手机上打开，但一般需要root权限和特殊软件。

原文地址：[戳这里](https://betacat.online/posts/2017-12-12/connect-adb-via-wifi/)
