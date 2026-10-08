import { getCollection } from 'astro:content';
import { SITE } from '../config';

export async function GET() {
  const posts = await getCollection('posts', ({ data }) => !data.draft);
  const tags = [...new Set(posts.flatMap(post => post.data.tags))];
  const paths = ['/', '/archives/', '/tags/', '/about/', ...posts.map(p => `/post/${p.data.slug}/`), ...tags.map(t => `/tag/${encodeURIComponent(t)}/`)];
  const body = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${paths.map(path => `\n  <url><loc>${SITE.url}${path}</loc></url>`).join('')}\n</urlset>`;
  return new Response(body, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
}
