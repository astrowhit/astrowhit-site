#!/usr/bin/env python3
"""
Downloads every remote image (and the CV PDF) referenced in this site's HTML
files, saves them under assets/images/ (and assets/docs/ for the PDF), and
rewrites every HTML file to point at the local copies instead of the original
astrowhit.com / Squarespace CDN URLs.

Run this from inside the astrowhit-site/ directory, on a machine with normal
internet access (this can't run inside the sandbox that built the site, since
its network is locked down):

    cd astrowhit-site
    python3 rehost_images.py

Safe to re-run: already-downloaded files are skipped.
"""
import os
import re
import sys
import urllib.request
import urllib.error

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(ROOT, "assets", "images")
DOC_DIR = os.path.join(ROOT, "assets", "docs")

URL_PATTERN = re.compile(
    r'https://images\.squarespace-cdn\.com/[^\s"\'<>]+'
    r'|https://www\.astrowhit\.com/s/[^\s"\'<>]+\.pdf'
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    )
}


def find_html_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if ".git" in dirpath.split(os.sep):
            continue
        for f in filenames:
            if f.endswith(".html"):
                yield os.path.join(dirpath, f)


def local_name_for(url):
    """Build a short, unique, readable local filename for a remote URL."""
    parts = [p for p in url.split("/") if p]
    basename = parts[-1]
    hash_part = parts[-2] if len(parts) >= 2 else ""
    hash_short = hash_part[-8:] if hash_part else ""
    # Strip query strings if any
    basename = basename.split("?")[0]
    if hash_short:
        return f"{hash_short}_{basename}"
    return basename


def download(url, dest_path):
    if os.path.exists(dest_path):
        return "skipped (already exists)"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp, open(dest_path, "wb") as out:
            out.write(resp.read())
        return "ok"
    except urllib.error.HTTPError as e:
        return f"failed (HTTP {e.code})"
    except Exception as e:
        return f"failed ({e})"


def main():
    os.makedirs(IMG_DIR, exist_ok=True)
    os.makedirs(DOC_DIR, exist_ok=True)

    html_files = list(find_html_files())
    all_urls = set()
    for path in html_files:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        all_urls.update(URL_PATTERN.findall(content))

    print(f"Found {len(all_urls)} unique remote URLs across {len(html_files)} HTML files.\n")

    url_to_relpath = {}  # url -> "assets/images/xyz.jpg" (relative to repo root)
    results = {"ok": 0, "skipped": 0, "failed": 0}
    failures = []

    for url in sorted(all_urls):
        is_pdf = url.lower().endswith(".pdf")
        name = local_name_for(url)
        dest_dir = DOC_DIR if is_pdf else IMG_DIR
        dest_path = os.path.join(dest_dir, name)
        rel_from_root = f"assets/{'docs' if is_pdf else 'images'}/{name}"

        status = download(url, dest_path)
        print(f"[{status:22s}] {url}")
        if status == "ok":
            results["ok"] += 1
        elif status.startswith("skipped"):
            results["skipped"] += 1
        else:
            results["failed"] += 1
            failures.append((url, status))

        url_to_relpath[url] = rel_from_root

    # Rewrite HTML files, adjusting relative depth for files not at repo root
    for path in html_files:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        depth = os.path.relpath(path, ROOT).count(os.sep)  # 0 for root files, 1 for news/*.html
        prefix = "../" * depth

        new_content = content
        for url, rel_from_root in url_to_relpath.items():
            if url in new_content:
                new_content = new_content.replace(url, prefix + rel_from_root)

        if new_content != content:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)

    print("\n--- Summary ---")
    print(f"Downloaded: {results['ok']}")
    print(f"Already present (skipped): {results['skipped']}")
    print(f"Failed: {results['failed']}")
    if failures:
        print("\nFailed URLs (still pointing at the original remote URL in the HTML):")
        for url, status in failures:
            print(f"  - {url} [{status}]")
    print("\nDone. Review with `git status` / `git diff`, then commit:")
    print('  git add -A && git commit -m "Rehost images and CV PDF locally"')


if __name__ == "__main__":
    main()
