---
title: Docker 学习笔记 （四） 数据管理
date: 2019-05-19T19:23:11+08:00
updated: 2020-07-05T13:27:32+08:00
tags:
  - docker
categories:
  - docker
---

![](http://ww3.sinaimg.cn/large/006tNc79gy1g36jt91zduj327w0r4168.jpg)



<!-- more -->



在默认情况下，容器内所有文件都存储在可写容器层中，这意味着：

- 当该容器不再存在时，数据不会持久存在，并且如果另一个容器需要数据，则可能很难从容器中获取数据。
- 容器的可写层紧密耦合到运行容器的主机。无法轻松地将数据移动到其他位置。
- 写入容器的可写层需要 存储驱动程序来管理文件系统。存储驱动程序使用Linux内核提供联合文件系统。与使用直接写入主机文件系统的数据卷相比，这种额外的抽象降低了性能 。

Docker有两个容器选项可以在主机中存储文件，因此即使在容器停止之后文件仍然会存在：volumes和 bind mounts。在Linux上运行Docker，可以使用tmpfs mount临时挂载。

无论哪种方式，数据在容器内都是相同的。它作为目录或容器文件系统中的单个文件公开。

Volumes，Bind mounts和tmpfs 装载之间差异的简单方法是考虑数据在Docker主机上的位置。

![](http://ww4.sinaimg.cn/large/006tNc79gy1g36owkutjrj30u00eyq5e.jpg)

### 三者的区别

- Volumes存储在由Docker（/var/lib/docker/volumes/在Linux上）管理的主机文件系统的一部分中。非Docker进程不应修改文件系统的这一部分。卷是在Docker中保留数据的最佳方式。
- Bind mounts可以存储在主机系统的任何位置。它们甚至可能是重要的系统文件或目录。Docker主机或Docker容器上的非Docker进程可以随时修改它们。
- tmpfs挂载仅存储在主机系统的内存中，永远不会写入主机系统的文件系统。

### Volumes的特点

卷是在Docker容器和服务中持久保存数据的首选方法。卷的一些用例包括：

- 在多个运行容器之间共享数据。如果未显式创建它，则会在第一次将其装入容器时创建卷。当该容器停止或被移除时，该卷仍然存在。多个容器可以同时安装相同的卷，可以是读写也可以是只读。仅在您明确删除卷时才会删除卷。
  
  当Docker主机不能保证具有给定的目录或文件结构时。卷可帮助您将Docker主机的配置与容器运行时分离。
- 如果要将容器的数据存储在远程主机或云提供程序上，而不是本地存储。
- 当您需要将数据从一个Docker主机备份，还原或迁移到另一个Docker主机时，卷是更好的选择。您可以使用卷停止容器，然后备份卷的目录（例如/var/lib/docker/volumes/）。

### Bind mounts的特点

- 将配置文件从主机共享到容器。这就是Docker默认通过/etc/resolv.conf从主机安装到每个容器中来为容器提供DNS解析的方式 。
- 在Docker主机上的开发环境和容器之间共享源代码或构建工件。例如，您可以将Maven target/ 目录挂载到容器中，每次在Docker主机上构建Maven项目时，容器都可以访问重建的工件。
  
  如果以这种方式使用Docker进行开发，您的生产Dockerfile会将生产就绪工件直接复制到映像中，而不是依赖于绑定装载。
- 当Docker主机的文件或目录结构保证与容器所需的绑定安装一致时。

### tmpfs

- tmpfs 不希望数据在主机或容器内持久存在时，最好使用挂载。这可能是出于安全原因，或者在应用程序需要编写大量非持久状态数据时保护容器的性能。

### Volumes和Bind mounts需要注意

- 如果将空卷装入容器中存在文件或目录的目录中，则会将这些文件或目录传播（复制）到卷中。同样，如果启动容器并指定尚不存在的卷，则会为您创建一个空卷。这是预先填充另一个容器所需数据的好方法。
- 如果将绑定装载或非空卷装入容器中存在某些文件或目录的目录中，则装载会遮盖这些文件或目录，就像将文件保存到/mntLinux主机上然后安装USB驱动器进入/mnt。/mnt在卸载USB驱动器之前，USB驱动器的内容会遮挡内容。隐藏的文件不会被删除或更改，但在安装绑定装载或卷时无法访问。

### 数据卷（Volumes）

数据卷 是一个可供一个或多个容器使用的特殊目录，它绕过 UFS，可以提供很多有用的特性：

- 数据卷 可以在容器之间共享和重用
- 对 数据卷 的修改会立马生效
- 对 数据卷 的更新，不会影响镜像
- 数据卷 默认会一直存在，即使容器被删除

> 注意：数据卷 的使用，类似于 Linux 下对目录或文件进行 mount，镜像中的被指定为挂载点的目录中的文件会隐藏掉，能显示看的是挂载的 数据卷。

#### 创建数据卷

```js
$ docker volume create my-vol
```

#### 查看所有的 数据卷

```js
 $ docker volume ls
DRIVER              VOLUME NAME
local               my-vol
```

#### 在主机里使用以下命令可以查看指定 数据卷 的信息

```js
$ docker volume inspect my-vol
[
    {
        "CreatedAt": "2019-05-19T08:22:09Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/my-vol/_data",
        "Name": "my-vol",
        "Options": null,
        "Scope": "local"
    }
]
```

#### 启动一个挂载数据卷的容器

在用 docker run 命令的时候，使用 -v和–mount 标记来将 数据卷 挂载到容器里。在一次 docker run 中可以挂载多个 数据卷。

##### -v或–mount的区别：

如果要指定数据卷的选项，则必须使用–mount。

- -v或–volume：由三个字段组成，用冒号字符（:）分隔。字段必须按正确的顺序排列，并且每个字段的含义不是很明显。
  
  - 对于命名卷，第一个字段是卷的名称，并且在给定主机上是唯一的。对于匿名卷，省略第一个字段。
  - 第二个字段是文件或目录在容器中安装的路径。
  - 第三个字段是可选的，是逗号分隔的选项列表，例如ro。这些选项将在下面讨论。
- –mount：由多个键值对组成，以逗号分隔，每个键=组由一个元组组成。该–mount语法比更详细的-v或–volume，但按键的顺序并不显著，并且标志的价值更容易理解。
  
  - type是挂载类型，可以是bind，volume，或 tmpfs。本主题讨论卷，因此挂载类型始终是volume。
  - source，对于命名卷，这是卷的名称。对于匿名卷，省略此字段。可以指定为source 或src。
  - destination 文件或目录在容器中的路径。可以指定为destination，dst或target。
  - readonly（如果存在）导致绑定装入以只读方式装入容器中。
  - volume-opt 选项可以多次指定，它采用由选项名称及其值组成的键值对。

> 注意：如果启动的容器不存在挂载卷的路径，Docker会自动创建。

- -v

```js
$ docker run -d \
  --name devtest \
  -v myvol2:/app \
  nginx:latest
```

- –mount

```js
$ docker run -d \
  --name devtest \
  --mount source=myvol2,target=/app \
  nginx:latest
```

#### 删除数据卷

删除容器后，Docker数据卷仍然存在。

- 例如，命名卷：具有来自容器外部的特定源awesome:/bar
- 匿名卷没有特定的源，因此在删除容器时，可以用–rm指令删除。

#### 删除匿名卷

要自动删除匿名卷，需要使用–rm选项。例如，创建匿名/foo卷。删除容器后，Docker守护进程会删除/foo卷但不会删除awesome卷。

```js
docker run --rm -v /foo -v awesome:/bar busybox top
```

#### 删除所有未使用的数据卷并释放空间：

```js
docker volume prune
```
