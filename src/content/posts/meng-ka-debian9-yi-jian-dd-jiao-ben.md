---
title: "萌咖debian9一键DD脚本"
slug: "meng-ka-debian9-yi-jian-dd-jiao-ben"
description: "DD系统 萌咖大佬已经成功测试DD脚本！这样我们比较方便的使用debian系统了！ 甲骨文原系统请选择 ubuntu16 （18系统兼容有一些问题！） 安装debian9脚本 (-firmware 额外驱动支持） curl支持，建议提前安装 CentOS： yum update -y && yum …"
publishedAt: "2022-08-11"
tags: ["重装系统", "DD"]
draft: false
featured: false
---
<p>DD系统<br/>
萌咖大佬已经成功测试DD脚本！这样我们比较方便的使用debian系统了！</p>
<p>甲骨文原系统请选择 ubuntu16 （18系统兼容有一些问题！）</p>
<p>安装debian9脚本 (-firmware 额外驱动支持）</p>
<p>curl支持，建议提前安装<br/>
CentOS：<br/>
yum update -y &amp;&amp; yum install curl -y</p>
<p>Debian/Ubuntu：<br/>
apt-get update -y &amp;&amp; apt-get install curl -y</p>
<!-- more -->
<p>bash &lt;(wget --no-check-certificate -qO- 'https://moeclub.org/attachment/LinuxShell/InstallNET.sh') -d 9 -v 64 -p 'RUYO' -a -firmware</p>
<!-- more -->
<p>适用于甲骨文，VIR等机器 （账号: root   密码:RUYO）</p>
<p>ubuntu进入设置密钥进入root用户<br/>
sudo passwd root<br/>
su<br/>
文献参考：https://moeclub.org/2018/04/03/603/<br/>
其他dd脚本：https://github.com/bin456789/reinstall</p>
