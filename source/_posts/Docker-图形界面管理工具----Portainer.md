---
title: Docker 图形界面管理工具 -- Portainer
date: 2019-05-19T13:02:34+08:00
updated: 2020-07-05T13:27:18+08:00
tags:
  - docker
categories:
  - docker
---

![](http://ww4.sinaimg.cn/large/006tNc79gy1g36jl1fll4j31fg0fkgnv.jpg)



<!-- more -->



[Portainer](https://github.com/portainer/portainer)（基于 Go）是一个轻量级的管理界面，可让您轻松管理Docker主机或Swarm集群。

Portainer的使用意图是简单部署。它包含可以在任何 Docker 引擎上运行的单个容器（Docker for Linux 和 Docker for Windows）。

Portainer允许您管理 Docker 容器、image、volume、network 等。 它与独立的 Docker 引擎和 Docker Swarm 兼容。

#### Docker 命令安装：

```js
docker volume create portainer_data

docker run -d -p 9000:9000 --name Portainer -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```

#### Swarm集群部署：

```js
$ docker volume create portainer_data
$ docker service create \
--name portainer \
--publish 9000:9000 \
--replicas=1 \
--constraint 'node.role == manager' \
--mount type=bind,src=//var/run/docker.sock,dst=/var/run/docker.sock \
--mount type=volume,src=portainer_data,dst=/data \
portainer/portainer \
-H unix:///var/run/docker.sock
```

#### Docker Compose 部署：

```js
version: '2'
services:
  portainer:
    image: portainer/portainer
    command: -H unix:///var/run/docker.sock
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data
volumes:
  portainer_data:
```

#### 使用

访问 [http://localhost:9000/](http://localhost:9000/)

![](http://ww4.sinaimg.cn/large/006tNc79gy1g36cm04aidj31i20u0466.jpg)
