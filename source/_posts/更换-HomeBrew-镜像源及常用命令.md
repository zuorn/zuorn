---
title: 更换 HomeBrew 镜像源及常用命令
date: 2019-05-22T08:49:58+08:00
updated: 2020-07-05T13:28:09+08:00
tags:
  - 工具
categories:
  - 工具
---

![](http://ww4.sinaimg.cn/large/006tNc79gy1g39tijtyf5j31fe0do0ut.jpg)

> 解决 brew install xxx 慢的问题。



<!-- more -->



HomeBrew 官网： [https://brew.sh](https://brew.sh)

## 更换brew镜像源

```plain
# 进入brew主目录
$ cd `brew --repo`

# 更换镜像
$ git remote set-url origin https://git.coding.net/homebrew/homebrew.git

# 测试效果
$ brew update
```

### 几个镜像:

- [https://git.coding.net/homebrew/homebrew.git](https://git.coding.net/homebrew/homebrew.git)
  
  - Coding
- [https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git](https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git)
  
  - 清华
- [https://mirrors.ustc.edu.cn/brew.git](https://mirrors.ustc.edu.cn/brew.git)
  
  - 中科大

### 参考：

- [Mac下更换Homebrew镜像源](https://blog.csdn.net/lwplwf/article/details/79097565)

## 附——常用命令

安装卸载

```plain
brew search text 搜索本地远程仓库的软件，已安装会显示绿色的勾
brew install <formula> 安装指定软件
brew unistall <formula 卸载指定软件
brew list 显示所有的已安装的软件
```

升级软件

```plain
brew update 自动升级homebrew（从github下载最新版本）
brew outdated 检测已经过时的软件
brew upgrade 升级所有已过时的软件，即列出的以过时软件
brew upgrade <formula>升级指定的软件
brew pin <formula> 禁止指定软件升级
brew unpin <formula> 解锁禁止升级
brew upgrade --all 升级所有的软件包，包括未清理干净的旧版本的包
```

清理相关

```plain
brew cleanup -n 列出需要清理的内容
brew cleanup <formula> 清理指定的软件过时包
brew cleanup 清理所有的过时软件
brew unistall <formula> 卸载指定软件
brew unistall <fromula> --force 彻底卸载指定软件，包括旧版本
```

#### 参考：[HomeBrew常规使用教程](https://juejin.im/post/5a559b9f6fb9a01cba42772f)
