---
title: docker run 后容器状态是 Exited 解析
date: 2019-05-22T16:21:13+08:00
updated: 2020-07-05T13:28:13+08:00
tags:
  - docker
categories:
  - docker
---

![](http://ww3.sinaimg.cn/large/006tNc79gy1g3a6eaacp1j31720c4tf9.jpg)



<!-- more -->



## 问题：

运行：`docker run -dit -p 4001:8888 -p 4002:3306 -v /Users/xinaogudu/hproxy:/usr/local/etc/haproxy --privileged --net=net1 --name h1 --ip 172.18.0.5  haproxy` 后容器状态是 `Exited`

## 解析：

> 容器的生命周期，要把 docker 容器看做是一个单独的进程及运行环境。容器不等价于一个虚拟的操作系统。Docker的开发人员也一直主张docker容器应该只运行一个进程。

再根据 [hproxy官方镜像](https://hub.docker.com/_/haproxy) 描述，镜像里是没有默认配置的，也就没有进程。这就不难解释为什么docker run 之后容器是 Exited 状态了。

[hproxy官方镜像](https://hub.docker.com/_/haproxy) 描述:

> Since no two users of HAProxy are likely to configure it exactly alike, this image does not come with any default configuration.

对于 hproxy 官方是推荐 build 创建自己的镜像然后 docker run 的时候直接指定配置文件的。

![](http://ww1.sinaimg.cn/large/006tNc79gy1g3a615jd6zj319b0u00vu.jpg)

## 解决：

所以解决办法有两种，一种是在 docker run 后加 bash 这样启动就有一个进程，容器就不是 Exited 状态了，另一种是按照官方的办法。build 自己的镜像然后再启动时指定文。

在 docker run 后加 bash ：

```plain
docker run -dit -p 4001:8888 -p 4002:3306 \
    -v /Users/xinaogudu/hproxy:/usr/local/etc/haproxy \
    --privileged \
    --net=net1 \
    --name h1 \
    --ip 172.18.0.5  \
    haproxy bash
```

#### 参考：

[Docker随笔记—docker run执行后，容器的状态是Exited的一些困惑](https://segmentfault.com/a/1190000010940432)
