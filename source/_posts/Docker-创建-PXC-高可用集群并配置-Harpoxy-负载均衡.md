---
title: Docker 创建 PXC 高可用集群并配置 Harpoxy 负载均衡
date: 2019-05-23T13:22:43+08:00
updated: 2020-07-05T13:28:26+08:00
tags:
  - dokcer
  - PXC
  - Haproxy
categories:
  - docker
---

![](http://ww4.sinaimg.cn/large/006tNc79gy1g3b6n7xz6kj327w0j8qah.jpg)



<!-- more -->



## 创建 PXC 集群环境

### 拉取 percona-xtradb-cluster 镜像

官方镜像地址：[https://hub.docker.com/r/percona/percona-xtradb-cluster](https://hub.docker.com/r/percona/percona-xtradb-cluster)

```plain
docker pull percona/percona-xtradb-cluster
```

percona/percona-xtradb-cluster 太长，我们换个名字叫做pxc，操作如下：

```plain
docker tag percona/percona-xtradb-cluster pxc
```

并将开始拉去的镜像删除，操作如下：

```plain
docker rmi percona/percona-xtradb-cluster
```

#### 创建docker网络

出于安全考虑，将PXC集群放置于docker内部网络中。只需将宿主的端口与之映射并开放出来即可。

```plain
docker network create --subnet=172.18.0.0/24 net1
```

其中，–subnet=172.18.0.0/24自定义网段172.18.0.0，24是指24位子网掩码 net1 网段名称。

执行成功后，我们可以通过`sudo docker inspect net1`查看内部网络信息。

#### 创建docker卷

docker容器的运行规则：通过目录映射的方法，将业务数据写入到宿主机中。好处是如果容器故障，只需将容器删除，重新启用一个容器即可，这样就不会丢失原来的数据。 由于PXC较为特殊，无法直接使用映射目录的方法做映射（使用后会闪退），故使用docker卷。 在命令行使用如下命令：

```plain
docker volume create --name v1
docker volume create --name v2
docker volume create --name v3
```

计划创建3个数据库节点，所以这里对应创建3个数据卷。

### 创建第一个容器节点：

```plain
docker run -d -p 3306:3306 -v v1:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=123456 \
    -e CLUSTER_NAME=PXC \
    -e XTRABACKUP_PASSWORD=123456 \
    --privileged \
    --name=node1 \
    --net=net1 \
    --ip 172.18.0.2 \
    pxc
```

> -d 默认在后台运行, -p 3306（宿主）:3306（容器） 端口映射，将容器3306端口映射到宿主3306端口 -v 目录映射，将第四步创建的v1映射到容器/var/lib/mysql -e MYSQL_ROOT_PASSROWD 创建的用户实例的密码，默认实例root -e CLUSTER_NAME 集群名称， -e XTRABACKUP_PASSWORD 数据库之间同步使用的密码 –privileged 权限.给予最高权限 –name 给容器容命名 –net 使用内部网段 –ip 内部网段分到的地址

#### 测试连接：

需要注意的是容器启动的速度虽然很快，但是pxc初始化是需要一点时间的（大概两分钟左右），必须等第一个容器初始化完成后再启动第二个pxc容器，不然会报错。

测试连接成功后就可以启动其他pxc容器了

在启动其他容器的时候需要更改映射的宿主机端口、容器的名称，还有指定 IP 地址。

### 创建第二个容器节点：

> 注意：在启动其他容器的时候需要更改映射的宿主机端口、容器的名称，还有指定 IP 地址。
>
> -e CLUSTER_JOIN=node1 用于连接第一个数据库节点

```plain
docker run -d -p 3307:3306 -v v2:/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD=123456 \
-e CLUSTER_NAME=PXC \
-e XTRABACKUP_PASSWORD=123456 \
-e CLUSTER_JOIN=node1 \
--privileged \
--name=node2 \
--net=net1 \
--ip 172.18.0.3 \
pxc
```

### 创建第三个容器节点：

```plain
docker run -d -p 3308:3306 -v v3:/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD=123456 \
-e CLUSTER_NAME=PXC \
-e XTRABACKUP_PASSWORD=123456 \
-e CLUSTER_JOIN=node1 \
--privileged \
--name=node3 \
--net=net1 \
--ip 172.18.0.4 \
pxc
```

#### 测试：

用数据库连接工具连接三个数据库，在node创建数据库`test`

```sql
CREATE database test;
```

如果其他数据库都同步过来那就没有问题了。

![](http://ww3.sinaimg.cn/large/006tNc79gy1g3a21d0wupj30si0b2jsk.jpg)

## Harpoxy 负载均衡

![](http://ww1.sinaimg.cn/large/006tNc79gy1g3a1w7txi0j31dk0maagw.jpg)

### 创建 haproxy 配置文件，并放到指定的宿主机目录。

```plain
global
        #工作目录
        chroot /usr/local/etc/haproxy
        #日志文件，使用rsyslog服务中local5日志设备（/var/log/local5），等级info
        log 127.0.0.1 local5 info
        #守护进程运行
        daemon

defaults
        log     global
        mode    http
        #日志格式
        option  httplog
        #日志中不记录负载均衡的心跳检测记录
        option  dontlognull
        #连接超时（毫秒）
        timeout connect 5000
        #客户端超时（毫秒）
        timeout client  50000
        #服务器超时（毫秒）
        timeout server  50000

#监控界面   
listen  admin_stats
        #监控界面的访问的IP和端口
        bind  0.0.0.0:8888
        #访问协议
        mode        http
        #URI相对地址
        stats uri   /dbs
        #统计报告格式
        stats realm     Global\ statistics
        #登陆帐户信息
        stats auth  admin:123456
#数据库负载均衡
listen  proxy-mysql
        #访问的IP和端口
        bind  0.0.0.0:3306  
        #网络协议
        mode  tcp
        #负载均衡算法（轮询算法）
        #轮询算法：roundrobin
        #权重算法：static-rr
        #最少连接算法：leastconn
        #请求源IP算法：source
        balance  roundrobin
       #日志格式
        option  tcplog
        #在MySQL中创建一个没有权限的haproxy用户，密码为空。Haproxy使用这个账户对MySQL数据库心跳检测
        option  mysql-check user haproxy
        server  MySQL_1 172.18.0.2:3306 check weight 1 maxconn 2000  
        server  MySQL_2 172.18.0.3:3306 check weight 1 maxconn 2000  
        server  MySQL_2 172.18.0.4:3306 check weight 1 maxconn 2000  
        #使用keepalive检测死链
        option  tcpka
```

### 启动 haproxy 容器

> /Users/xinaogudu/hproxy 是我放置配置文件的目录。

```plain
docker run -dit -p 4001:8888 -p 4002:3306 \
-v /Users/xinaogudu/hproxy:/usr/local/etc/haproxy \
--privileged \
--net=net1 \
--name h1 \
--ip 172.18.0.5 \
haproxy
```

### 进入 haproxy 容器指明配置文件

```plain
docker exec -it h1 bash
```

```plain
# 指定 haproxy 配置文件位置
haproxy -c -f /usr/local/etc/haproxy/haproxy.cfg
```

### 在数据库中创建一个没有密码的 haproxy 用户用于心跳检测。

```plain
create user 'haproxy'@'%' identified by '';
```

## 验证

### 登录 haproxy 监控：[http://localhost:4001/dbs](http://localhost:4001/dbs)

![](http://ww3.sinaimg.cn/large/006tNc79gy1g3b67er48cj327y0tqwoh.jpg)

### 用数据库管理工具连接 haproxy 端口测试：

![](http://ww3.sinaimg.cn/large/006tNc79gy1g3b6ajpic6j317m0sq43v.jpg)
