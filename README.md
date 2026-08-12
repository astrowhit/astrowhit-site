# astrowhit-site

This is a static HTML/CSS recreation of [astrowhit.com](https://www.astrowhit.com), the personal/academic website of **Prof. Katherine E. Whitaker**, Professor of Astronomy at UMass Amherst. It was built so the site can be hosted for free on **GitHub Pages** instead of Squarespace.

## How this was built

The content was produced by fetching the live Squarespace pages at astrowhit.com (Home, Research Group, Research, Curriculum Vitae, Publications, Teaching, Outreach, Mentoring Resources, and the News archive, including up to the 30 most recent individual news posts) and reproducing the text, structure, and links faithfully in plain HTML with a single shared stylesheet (`assets/css/style.css`).

**Squarespace content changes over time.** Because this was a point-in-time snapshot, please periodically re-check the live site (astrowhit.com) against this repo and update facts, dates, publication lists, and news posts as needed — especially the CV, Publications, and News sections, which change most frequently.

## Site structure

```
astrowhit-site/
  index.html                 Home
  research-group.html
  research.html
  cv.html
  publications.html
  teaching.html
  outreach.html
  mentoring-resources.html
  news/
    index.html                List of all mirrored news posts
    <slug>.html                One page per news post (30 most recent)
  assets/
    css/style.css              Shared stylesheet for every page
    images/                     (currently empty — see Known Limitations)
    docs/                       (currently empty — see Known Limitations)
  README.md
```

Every page shares the same hand-written header (site title, tagline, nav bar, Twitter/X link) and footer (contact block) — there is no templating system or build step; it's plain static HTML, which keeps it simple to host and edit directly on GitHub.

## Publishing to GitHub Pages

From inside this `astrowhit-site/` directory (git has already been initialized and the first commit made):

```bash
git remote add origin <your-new-github-repo-url>
git branch -M main
git push -u origin main
```

Then on GitHub:

1. Go to your repository's **Settings** tab.
2. Click **Pages** in the left sidebar.
3. Under "Build and deployment," set **Source** to "Deploy from a branch."
4. Set **Branch** to `main` and the folder to `/ (root)`.
5. Save. GitHub will give you a URL like `https://<username>.github.io/<repo-name>/` within a few minutes.

If you'd like the site to live at a custom domain (e.g. astrowhit.com itself), add a `CNAME` file at the repo root containing the domain name, and point your domain's DNS at GitHub Pages per [GitHub's custom domain docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).

## Known limitations / differences from the live site

- **Images were not downloaded locally.** The build environment's network sandbox blocks outbound requests to `images.squarespace-cdn.com` (and, in fact, to nearly every external domain except a short allow-list of package registries like pypi.org and github.com) via a `blocked-by-allowlist` proxy rule. Every `curl` attempt to fetch an image or the CV PDF returned HTTP 403. As a result, **all images across every page link directly to the original `images.squarespace-cdn.com` URLs** rather than to local copies in `assets/images/`. This means the site currently depends on Squarespace continuing to host those images — if that ever changes, images will break. If you have local access to run this from a machine with normal internet access, re-run a proper `curl -L -o assets/images/<name> <url>` pass over all image URLs referenced in the HTML and update the `src` attributes to relative paths.
- **CV PDF was not downloaded.** For the same network-sandbox reason, the "Download PDF Version Here" link on `cv.html` points to the original `https://www.astrowhit.com/s/cv_whitaker_may2025_nopublications_general.pdf` rather than a local copy in `assets/docs/`.
- **Publications list is incomplete below entry [105].** The live `/publications` page is extremely long (~220+ entries). The fetch tool used to retrieve it truncated consistently at roughly the same point across repeated attempts (~66.8K characters), capturing the "Submitted Works" section plus published entries **[222] down to [106]** (2025 back through 2021). Entries **[105] and earlier** — 2020 and before, back to the start of Prof. Whitaker's career around 2010 — could not be reliably retrieved and were deliberately omitted rather than guessed at. `publications.html` calls this out explicitly and links to the live page and the complete ADS author search as the authoritative source for the rest.
- **News: only the 30 most recent posts were mirrored.** `news/index.html` lists all 30 with links to locally-built pages; older posts are not mirrored and the live news archive is linked instead.
- **No CMS, search, comments, or contact form.** The original Squarespace site has a `/search` page, a commenting system on news posts, and various Squarespace-specific interactive blocks (image galleries with lightboxes, "View fullsize" overlays, etc.). None of that dynamic functionality exists here — image galleries are simple flexbox grids of `<img>` tags, and there is no search or comment functionality. The "Data Challenge," "Astronomy Research Tutorial Repository," and a few other linked Squarespace-hosted pages referenced from Teaching/Outreach/Mentoring Resources were not pages this build was asked to mirror, and those links still point to astrowhit.com.
- **Visual design does not match Squarespace.** As specified in the build brief, this uses a clean, original academic-style layout (serif headings, generous whitespace, responsive CSS in `assets/css/style.css`) rather than trying to pixel-match the Squarespace template, which is expected to change anyway.
- **Some homepage banner images were skipped.** A handful of images referenced in the original build brief (`banner_uncover.png`, `16635409814_684de15b6b_o.jpg`, `IMG_5247.JPG`, `Whitaker_eclipse.jpg`, `Whitaker_DAWN22.jpeg`, `IMG_2872_crop.jpg`) did not have confirmed source URLs available and were intentionally left out of the homepage image strip rather than guessed.

## Content accuracy

Every fact, name, date, and publication detail reproduced here was taken directly from the live astrowhit.com pages (or, where noted above, deliberately left out rather than invented). If you spot anything that has since changed on the live site, please update the corresponding HTML file directly — there's no database or CMS to sync from.
