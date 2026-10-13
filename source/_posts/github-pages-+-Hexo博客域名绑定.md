---
title: github pages + Hexo博客域名绑定
date: 2018-04-13T16:59:00+08:00
updated: 2019-10-17T12:24:39+08:00
tags:
  - Hexo
categories:
  - Hexo
---

## 终于有自己的域名了！

![](http://ovlnt0xy1.bkt.clouddn.com/2018-04-13-15236108756974.jpg)



<!-- more -->



经过几番折腾，终于绑定好了域名，现在总结一下

#### 申请个人域名：

- 首先你要有个域名，在
  
  [万网](https://wanwang.aliyun.com/)
  
  购买即可。（当然要注册阿里云账号。）
- **域名实名认证**
  
  ，具体看
  
  [这里](https://help.aliyun.com/knowledge_detail/48263.html?spm=a2c4g.11186623.2.26.rUjij3)
  
  。
- 在
  
  [域名信息查询（WHOIS）](https://whois.aliyun.com/?spm=5176.whzuorntop.10.4.218b39c62rDWWb)
  
  确保自己的域名状态正常（如图）就可以开始配置啦！
  
  
  
  
  ![](http://ovlnt0xy1.bkt.clouddn.com/2018-04-13-15236121614574.jpg)

#### 域名添加dns解析：

- 添加记录类型为
  
  `CNAME`
  
  、主机记录为
  
  `www`
  
  、记录值为自己github二级域名的解析。
- 添加记录类型为
  
  `A`
  
  、主机记录为
  
  `@`
  
  、记录值为自己github的ip地址的解析。

通过ping 自己的gihub二级域名可获取ip
![](http://ovlnt0xy1.bkt.clouddn.com/2018-04-13-15236134421366.jpg)

![](http://ovlnt0xy1.bkt.clouddn.com/2018-04-13-15236126374864.jpg)
添加完成勾选点击启用，状态为–即可。

#### 创建CNAME文件：

在hexo本地目录`source`下新建CNAME（无后缀）文件并填入自己的域名，比如：

```js
zuorn.top
www.zuorn.top
```

重新生成上传：

```bash
hexo d -g
```

#### github域名绑定：

打开博客在github中的地址，点击`Settings`，修改`Custom domain`为我们自己的域名保存即可。

![](http://ovlnt0xy1.bkt.clouddn.com/2018-04-13-15236140425982.jpg)

这个时候在浏览器当中输入域名就可以顺利打开了。

![](http://ovlnt0xy1.bkt.clouddn.com/2018-04-13-15236143444491.jpg)
