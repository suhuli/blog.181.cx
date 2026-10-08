# 速狐博客

`https://blog.181.cx` 的全新静态博客源码。

- Astro 生成纯静态 HTML
- GitHub Pages 托管
- Markdown 文章与图片全部保存在本仓库
- GitHub Actions 自动构建并发布到 `gh-pages`
- 管理后台位于 `https://bk.181.cx`，后端源码在私有仓库 `suhuli/bk-api`

## 本地开发

要求 Node.js `>=22.12`。

```bash
npm ci
npm run dev
npm run build
```

## 内容结构

```text
src/content/posts/       Markdown 文章
public/images/posts/     文章图片
src/pages/               页面与路由
src/layouts/             页面布局
src/styles/              全局样式
```

文章 frontmatter 示例：

```yaml
---
title: "文章标题"
slug: "article-slug"
description: "摘要"
publishedAt: "2026-10-08"
tags: ["Cloudflare", "教程"]
draft: false
featured: false
---
```

## 部署

推送到 `main` 后，`.github/workflows/deploy.yml` 会：

1. 使用 Node.js 22 安装依赖；
2. 构建 Astro 静态站；
3. 将 `dist/` 发布到 `gh-pages`；
4. 保留自定义域名 `blog.181.cx`。

GitHub Pages 应设置为从 `gh-pages` 分支根目录部署。

## 旧站迁移

原有 9 篇 Gridea 文章已经迁移，原 `/post/<slug>/` 地址保持不变。旧图片已转换为 WebP，迁移后的文章图片约 456 KB。
