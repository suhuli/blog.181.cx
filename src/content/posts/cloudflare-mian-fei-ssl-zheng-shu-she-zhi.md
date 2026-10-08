---
title: "Cloudflare免费ssl证书设置"
slug: "cloudflare-mian-fei-ssl-zheng-shu-she-zhi"
description: "Cloudflare设置ssl加密状态，分为三种。 OFF（关闭）：没有访问者能够通过HTTPS查看您的网站; 他们将被重定向到HTTP。 Flexible SSL（灵活的SSL）：即使使用对您的站点无效的证书，也无法在您的原始设备上配置HTTPS支持。访问者将能够通过HTTPS访问您的网站，但通过…"
publishedAt: "2021-09-03"
tags: ["CDN"]
draft: false
featured: false
---
<p>Cloudflare设置ssl加密状态，分为三种。<br/>
OFF（关闭）：没有访问者能够通过HTTPS查看您的网站; 他们将被重定向到HTTP。</p>
<p>Flexible SSL（灵活的SSL）：即使使用对您的站点无效的证书，也无法在您的原始设备上配置HTTPS支持。访问者将能够通过HTTPS访问您的网站，但通过HTTP连接到您的来源。注意：您可能会遇到一些带有一些原点配置的重定向循环。</p>
<p>Full SSL（完整SSL）：您的源支持HTTPS，但安装的证书与您的域不匹配或者是自签名的。Cloudflare将通过HTTPS连接到您的来源，但不会验证证书。</p>
<p>Full SSL (strict)（完全SSL（严格））：您的原产地有安装的有效证书（未过期并由受信任的CA或Cloudflare Origin CA签署）。Cloudflare将通过HTTPS连接并验证每个请求的证书。</p>
