---
title: "esim卡euicc问题列表"
slug: "esim-qia-euicc-wen-ti-lie-biao"
description: "卡片是400k，每个esim profile的大小差不多是20~30k，这样最多同时能写入大概是20个，多了只能删掉旧的。（寿命保守估计3-5年） Q：通知有什么用？在哪里看？ A：其实这个通知是发送给运营商的，让运营商知道你对esim配置进行了一些操作。 Q：那我能不能不发送通知？ A：当然可以。…"
publishedAt: "2025-02-05"
tags: []
draft: false
featured: false
---
<p>卡片是400k，每个esim profile的大小差不多是20~30k，这样最多同时能写入大概是20个，多了只能删掉旧的。（寿命保守估计3-5年）</p>
<p>Q：通知有什么用？在哪里看？</p>
<p>A：其实这个通知是发送给运营商的，让运营商知道你对esim配置进行了一些操作。</p>
<p>Q：那我能不能不发送通知？</p>
<p>A：当然可以。但是有部分运营商只有收到了“安装通知”后才允许你接入基站，也有一部分运营商（比如“CTM”）只有收到了“删除通知”（也就是“联网删除”），才允许你把esim配置写入其他设备。</p>
<p>Q：正常勾选哪几个？</p>
<p>A：按照标准来说，应该全部勾选。类似iPhone的原生esim管理，就是自动发送并移除通知的。但是“启用通知”和“禁用通知”，似乎运营商也不在意，开启之后切卡速度会变慢。</p>
<p>Q：那为什么默认选项不勾选“并移除”呢？</p>
<p>A：这是因为之前有部分群友，遇到部分运营商（比如“OneNZ”）发送删除通知，运营商由于网络问题没能收到。这就导致配置已经被删除了，但是不是“联网删除”。所以无法下载新的配置文件。这就需要和客服沟通解决或者去营业厅处理了。如果MiniLPA软件还没有移除通知，那你还能再发一遍（或多遍）。通知这玩意儿，用MiniLPA作者的话说：“你胆子大不怕卡丢了，随便删”。</p>
<p>补一下重新发送通知的操作：右击需要重新发送的通知，点击“发送”按钮即可。</p>
<p>我们在购买eSIM后，一般会收到一个二维码，正常手机扫码后就可以安装eSIM，而5ber则是使用官方App扫码。其实这个二维码的内容很简单，格式如下：<br/>
格式<br/>
LPA:1<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi><mi>M</mi><mo>−</mo><mi>D</mi><mi>P</mi><msub><mo>+</mo><mi>A</mi></msub><mi>D</mi><mi>D</mi><mi>R</mi><mi>E</mi><mi>S</mi><mi>S</mi></mrow><annotation encoding="application/x-tex">{SM-DP+_ADDRESS}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="base"><span class="strut" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathdefault" style="margin-right:0.05764em;">S</span><span class="mord mathdefault" style="margin-right:0.10903em;">M</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord mathdefault" style="margin-right:0.02778em;">D</span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin"><span class="mbin">+</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">A</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord mathdefault" style="margin-right:0.02778em;">D</span><span class="mord mathdefault" style="margin-right:0.02778em;">D</span><span class="mord mathdefault" style="margin-right:0.00773em;">R</span><span class="mord mathdefault" style="margin-right:0.05764em;">E</span><span class="mord mathdefault" style="margin-right:0.05764em;">S</span><span class="mord mathdefault" style="margin-right:0.05764em;">S</span></span></span></span></span>{MATCHING_ID}</p>
<p>SM-DP+_ADDRESS是一个域名，MATCHING_ID是一个id标示符。扫码以后，手机会带上MATCHING_ID，去SM-DP+_ADDRESS这个域名所在的服务器中下载对应的profile文件，并写入eUICC中。<br/>
<img alt="" decoding="async" loading="lazy" src="/images/posts/1738768730822.webp"/></p>
<p>很经典的一篇文章，可以说是奠基之作，必看：https://iecho.cc/2023/10/20/Convert-eSIM-to-physical-SIM/<br/>
合法eUICC CI证书id列表：https://euicc-manual.osmocom.org/docs/pki/ci/<br/>
eSTK.me: 下一代可插拔消费者 eSIM 卡：https://iecho.cc/2024/03/16/estk-me-next-generation-removable-consumer-esim/<br/>
EID列表：https://euicc-manual.osmocom.org/docs/pki/eum/</p>
