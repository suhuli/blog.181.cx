import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://blog.181.cx',
  output: 'static',
  trailingSlash: 'always',
  build: { format: 'directory' },
  markdown: {
    shikiConfig: { theme: 'github-dark-default', wrap: true }
  },
  vite: {
    server: { allowedHosts: true }
  }
});
