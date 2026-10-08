---
title: "cloudflared内网穿透实现Windows远程桌面"
slug: "cloudflared-nei-wang-chuan-tou-shi-xian-windows-yuan-cheng-zhuo-mian"
description: "提前准备 Cloudflare账号，注册地址：https://www.cloudflare.com 自定义域名并托管到Cloudflare（使用Freenom免费域名） 下载 Cloudflare可执行文件 下载地址：https://github.com/cloudflare/cloudflared…"
publishedAt: "2024-12-01"
tags: []
draft: false
featured: false
---
<p>提前准备<br/>
Cloudflare账号，注册地址：https://www.cloudflare.com<br/>
自定义域名并托管到Cloudflare（使用Freenom免费域名）<br/>
下载 Cloudflare可执行文件 下载地址：https://github.com/cloudflare/cloudflared/releases</p>
<p>被控端电脑配置<br/>
将 下载好的可执行文件(cloudflared-windows-amd64.exe) 复制到 自己定义的目录 并改短名称为(cloudflared.exe)，方便操作<br/>
在当前目录打开 cmd 窗口，输入如下命令进行登录验证，会自动打开游览器进行登录<br/>
cloudflared.exe login</p>
<p>登录完成之后会在 C:\Users%USERNAME%.cloudflared 目录下生成登录凭证<br/>
<img alt="" decoding="async" loading="lazy" src="/images/posts/1733066741280.webp"/></p>
<p>创建隧道，随意自定义名称<br/>
cloudflared.exe tunnel create <name></name></p>
<p>配置 DNS 记录（使用Freenom免费域名），就是上一步创建的隧道名称<br/>
cloudflared.exe tunnel route dns <name> diy.181.cx</name></p>
<p>配置完成之后，可以在控制台看到记录<br/>
<img alt="" decoding="async" loading="lazy" src="/images/posts/1733066853151.webp"/></p>
<p>在 cloudflared.exe 同级目录创建一个 config.yaml 文件，内容如下</p>
<h1 id="隧道的-uuid-就是登录凭证的json文件名称">隧道的 UUID, 就是登录凭证的json文件名称</h1>
<p>tunnel: xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx</p>
<h1 id="鉴权文件的全路径注意替换为自己的">鉴权文件的全路径，注意替换为自己的</h1>
<p>credentials-file: C:\Users%USERNAME%.cloudflared\xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx.json</p>
<p>ingress:</p>
<h1 id="你的freenom二级域名">你的freenom二级域名</h1>
<ul>
<li>hostname: diy.domain.cf<br/>
service: rdp://localhost:3389</li>
</ul>
<h1 id="默认错误404">默认错误404</h1>
<ul>
<li>service: http_status:404</li>
</ul>
