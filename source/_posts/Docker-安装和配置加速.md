---
title: Docker 安装和配置加速
date: 2019-04-06T12:11:15+08:00
updated: 2020-07-05T13:30:23+08:00
tags:
  - docker
categories:
  - docker
---

![](http://ww3.sinaimg.cn/large/006tNc79gy1g36jt91zduj327w0r4168.jpg)



<!-- more -->



Docker 分为 CE 和 EE 两大版本。CE 即社区版（免费，支持周期 7 个月），EE 即企业版，强调安全，付费使用，支持周期 24 个月。

Docker CE 分为 stable, test, 和 nightly 三个更新频道。每六个月发布一个 stable 版本 (18.09, 19.03, 19.09…)。

### 安装

Docker有多种安装方式本人推荐 Mac OS 和 windows 通过下载安装包安装，Linux使用官方的shell脚本安装。

#### Linux安装：

获取最新版本的 Docker 安装包并执行安装：

```js
wget -qO- https://get.docker.com/ | sh
```

启动 docker 服务：

```js
sudo service docker start
```

#### Mac OS安装：

下载安装文件： [https://hub.docker.com/editions/community/docker-ce-desktop-mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac)

和其他软件一样，双击并拖入应用程序目录即可。

#### windows 安装

下载安装文件：[https://hub.docker.com/editions/community/docker-ce-desktop-windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

和其他软件一样，双击下一步下一步即可。

#### 镜像加速

推荐加速服务：

- docker中国：
  
  [https://registry.docker-cn.com](https://registry.docker-cn.com)
- [阿里云加速器（需要账号获取）](https://account.aliyun.com/login/login.htm?oauth_callback=https%3A%2F%2Fcr.console.aliyun.com%2Fcn-hangzhou%2Fmirrors)
- [七牛云加速器 https://reg-mirror.qiniu.com](https://kirk-enterprise.github.io/hub-docs/#/user-guide/mirror)

##### Linux

对于使用 systemd 的系统，请在 /etc/docker/daemon.json 中写入如下内容（如果文件不存在请新建该文件）

```js
{
  "registry-mirrors": [
    "https://registry.docker-cn.com"
  ]
}
```

重新启动docker服务

```js
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
```

##### Windows

使用 Windows 10 的系统，在系统右下角托盘 Docker 图标内右键菜单选择 Settings，打开配置窗口后左侧导航菜单选择 Daemon。在 Registry mirrors 一栏中填写加速器地址 [https://registry.docker-cn.com，之后点击](https://registry.docker-cn.com，之后点击) Apply 保存后 Docker 就会重启并应用配置的镜像地址了。

##### Mac OS

使用 macOS 的用户，在任务栏点击 Docker Desktop 应用图标 -> Perferences… -> Daemon -> Registry mirrors。在列表中填写加速器地址 [https://registry.docker-cn.com。修改完成之后，点击](https://registry.docker-cn.com。修改完成之后，点击) Apply & Restart 按钮，Docker 就会重启并应用配置的镜像地址了。

#### 检查是否生效

执行 `docker info` ，如果从结果中看到了如下内容，说明配置成功。

```js
Registry Mirrors:
 https://registry.docker-cn.com
```
