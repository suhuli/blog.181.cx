#!/usr/bin/env python3
"""One-time migration from the generated Gridea site into Astro content."""
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image
import html
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT.parent / "legacy-blog"
POSTS = ROOT / "src/content/posts"
IMAGES = ROOT / "public/images/posts"
POSTS.mkdir(parents=True, exist_ok=True)
IMAGES.mkdir(parents=True, exist_ok=True)


def optimize_image(source: Path, target: Path, max_width=1600):
    with Image.open(source) as image:
        image.load()
        if image.width > max_width:
            height = round(image.height * max_width / image.width)
            image = image.resize((max_width, height), Image.Resampling.LANCZOS)
        if image.mode not in ("RGB", "RGBA"):
            image = image.convert("RGBA" if "transparency" in image.info else "RGB")
        target.parent.mkdir(parents=True, exist_ok=True)
        image.save(target, "WEBP", quality=82, method=6)


image_map = {}
for source in (LEGACY / "post-images").glob("*"):
    if source.is_file():
        target_name = f"{source.stem}.webp"
        try:
            optimize_image(source, IMAGES / target_name)
            image_map[source.name] = f"/images/posts/{target_name}"
        except Exception:
            target = IMAGES / source.name
            shutil.copy2(source, target)
            image_map[source.name] = f"/images/posts/{source.name}"

avatar = LEGACY / "images/avatar.png"
if avatar.exists():
    optimize_image(avatar, ROOT / "public/images/avatar.webp", max_width=320)
shutil.copy2(LEGACY / "favicon.ico", ROOT / "public/favicon.ico")

for page in sorted((LEGACY / "post").glob("*/index.html")):
    slug = page.parent.name
    if slug == "about":
        continue
    soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
    title_node = soup.select_one(".post-detail > .post-title")
    date_node = soup.select_one(".post-detail > .post-date")
    content_node = soup.select_one(".post-content")
    if not all((title_node, date_node, content_node)):
        print(f"skip {slug}: missing required fields")
        continue

    title = title_node.get_text(" ", strip=True)
    published = date_node.get_text(strip=True)
    tags = [tag.get_text(" ", strip=True) for tag in soup.select(".tag-container .tag")]

    for img in content_node.select("img"):
        src = img.get("src", "")
        name = src.rsplit("/", 1)[-1].split("?", 1)[0]
        if name in image_map:
            img["src"] = image_map[name]
        img["loading"] = "lazy"
        img["decoding"] = "async"

    # Turn bare absolute URLs in text nodes into Markdown-friendly links only when safe.
    body = content_node.decode_contents().strip()
    body = body.replace("https://blog.181.cx/post-images/", "/images/posts/")
    text = content_node.get_text(" ", strip=True)
    description = re.sub(r"\s+", " ", text)[:150]
    if len(text) > 150:
        description += "…"

    frontmatter = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"slug: {json.dumps(slug, ensure_ascii=False)}",
        f"description: {json.dumps(description, ensure_ascii=False)}",
        f"publishedAt: {json.dumps(published)}",
        f"tags: {json.dumps(tags, ensure_ascii=False)}",
        "draft: false",
        "featured: false",
        "---",
        "",
    ]
    (POSTS / f"{slug}.md").write_text("\n".join(frontmatter) + body + "\n", encoding="utf-8")
    print(f"migrated {slug}")

print(f"Migrated {len(list(POSTS.glob('*.md')))} posts; optimized {len(image_map)} images")
