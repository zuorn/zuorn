---
title: Docker学习笔记
date: 2019-04-06T23:07:29+08:00
updated: 2020-07-05T13:27:53+08:00
tags:
  - docker
categories:
  - docker
---

![](http://ww3.sinaimg.cn/large/006tNc79gy1g36jt91zduj327w0r4168.jpg)



<!-- more -->



### 基础命令

- 启动容器：
  
  `docker run -dit ubuntu`
- 查看建立的容器：
  
  `dokcer inspect`
- 自定义容器名：
  
  ```js
  dokcer run --name=自定义名 -i -t IMAGE /bin/bash
  ```
- 重新启动停止的容器：
  
  `docker start [-i] 容器名`
  
  。 -i是以交互的方式启动停止的容器
- 删除已经停止的容器：
  
  `docker rm 容器名`

### 守护式容器

> 能够长期运行
> 没有交互式会话
> 适合运行应用程序和服务

- 以守护式运行容器：

```js
docker run -i -t IMAGE /bin/bash
同时按ctrl+P和ctrl+q //退出后容器在后台运行
```

- 附加到运行中的容器：
  
  `docker attach 容器名`
- 启动守护式容器：

```shell
//-d 使用后台的方式来执行命令
docker run -d 镜像名 [COMMAND] [ARG...]
``` 
* 查看容器日志：

```js
docker logs [-f] [-t] [--tail] 容器名
	-f --follows=true|false 默认false
	-t timestamps=true|false 默认false
	--tail="all"
```

- 查看容器内进程：

```js
docker top 容器名
```

- 在运行中的容器内启动新进程：

```js
docker exec [-d] [-i] [-t] 容器名 [COMMAND] [ARG...]
```

- 停止守护式容器：
  
  备注：重启容器后容器的ip和端口映射都会发生改变。

```js
docker stop 容器名 //发送一个信号给容器，等待停止
docker kill 容器名 //直接停止容器
```

### 设置容器的映射端口

#### 端口映射

```js
run [-P] [-p]

//将为容器暴露的所有端口进行映射
-P,publish-all=true | false 默认为false
	docker run -P -i-t ubuntu /bin/bash
	
//指定映射端口
-p,--publish=[]

containerPort //只制定容器的端口（宿主机的端口是随机映射的）
	docker run -p 8080:80 -i -t ubuntu /bin/bash

hostPort:containnerPort //同时指定宿主机的端口和容器的端口（一一对应）
	docker run -p 8080:80 -i -t ubuntu /bin/bash
	
ip::containerPort //指定ip和容器的端口
	docker run -p 0.0.0.0:80 -i -t ubuntu /bin/bash
	
ip:hostPort:containerPort //ip、宿主机端口和容器端口都进行指定
	docker run -p 0.0.0.0:8080:80 -i -t ubuntu /bin/bash
```

#### 查看端口映射

```js
dokcer port 容器名
```

#### 练习：在容器中部署静态网站

```text
//创建映射80端口的交互式容器
docker run -p 80 --name=web -i -t b2ab0ed558bb /bin/bash    
//安装Nginx
yum install -y nginx

//安装文本编辑器vim
yum install vim

//验证网站访问
docker port web //查看端口
```

### 镜像

- 列出镜像

```js
docker images [OPTSIONS][REPOSITORY]
		-a,--all=false  //默认不显示中间层的镜像
		-f,--filter=[]  //显示时的过滤条件
		--no-trunc=false  //不使用截断的形式来显示数据（默认会截断唯一id）
		-q,--quiet=false  //只显示镜像的唯一id
```

- 镜像的仓库
  
  REPOSITORY 仓库 镜像的集合
- TAG 标签 默认使用latest标签
- 查看镜像的详细信息(inspect也支持容器的查看)

```js
docker inspect [OPTIONS]CONTAINER|IMAGE[CONTAINER|IMAGE...]
	-f,format=""
```

- 删除镜像

```js
docker rmi [OPTIONS]IMAGE[IMAGE...]
	-f,--force=false 强制删除镜像
	--no-prune=false 会保留被删镜像中被打标签的父镜像
```

### 获取和推送镜像

- 查找镜像
  
  
  
  
  Docker Hub
  
  
  
  
  [https://registry.hub.docker.com](https://registry.hub.docker.com)

```js
docker search [OPTIONS]TERM
	--automated=false
	--no-trunc=false 
	-s,--stars=0
```

- 拉取镜像

```js
docker pull [OPTIONS] NAME[:TAG]
	-a,all-tags=false 下载全部标记的镜像
```

- 推送镜像

```js
docker push NAME[:TAG]
```

### 构建镜像

> 保存对容器的修改，并再次使用
> 自定义镜像的能力
> 以软件的形式打包并分发服务及其运行环境

- 通过容器构建

会暂停正在使用的容器

```js
	docker commit [OPTIONS] CONTAINER [REPOSITORY][:TAG]
		-a,--author=""  镜像的作者
		-m,-message="" 镜像构建的信息
		-p,--pause=true 可以不暂停正在使用的容器
	```	

* 通过Dockerfile文件构建

	1. 创建Dockerfile文件
	
	2. 运行docker build命令

```js
	docker build [OPTIONS] PATH | URL | -
		--force-rm=false
		--no-cache=false
		-pull==false
		-q,--quiet=false
		--rm=true
		-t,--tag=""
```

### dockerC/S模式

```text
![](https://ws4.sinaimg.cn/large/006tNc79ly1g1tbggmcy8j317s0nsnbb.jpg)
```

![](https://ws1.sinaimg.cn/large/006tNc79ly1g1tbg4n0arj317e0e01ft.jpg)

#### Remote API

- RESTful风格API
- STDIN、STDOUT、STDERR
  ![](https://ws1.sinaimg.cn/large/006tNc79ly1g1tbfr9f67j317g0ewx25.jpg)
- Docker官方的Remote APO Reference:
  
  [https://docs.docker.com/reference/api/docker_remote_api/](https://docs.docker.com/reference/api/docker_remote_api/)

#### 连接方式（客户端与服务端的守护进程）

![](https://ws2.sinaimg.cn/large/006tNc79ly1g1tbf671nlj316o0c2qet.jpg)

- unix://var/run/docker.sock
- tcp://host:port
- fd://socketfd

### Docker守护进程的配置和操作

- 查看守护进程

```js
ps -ef |grep docker
sudo status docker
```

- 使用service命令管理

```js
启动
sudo service docker start

停止
sudo service docker stop

重启
sudo service docker restart
```
