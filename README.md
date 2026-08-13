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
- **CV PDF is hosted locally.** `assets/docs/cv_whitaker_may2025_nopublications_general.pdf` is the user-supplied copy; `cv.html` links to it directly.
- **REU Programs PDF is hosted locally.** `assets/docs/REU-Programs.pdf` is the user-supplied copy; `mentoring-resources.html` links to it directly instead of astrowhit.com.
- **Publications list is up to date as of August 2026.** `publications.html` includes 243 refereed publications plus 26 submitted/in-review works, each linked to ADS, organized by year back to 2005. This was reconciled against a full ADS BibTeX export of Katherine E. Whitaker's author record: entries that moved from "Submitted Works" to a refereed journal were re-filed with updated journal citations, and 31 genuinely missing Whitaker-coauthored papers (13 published, 18 still preprints) turned up in the export and were added. About a dozen other name matches in that export (HAWC/gamma-ray physics, marine biology, aerospace engineering, etc.) were excluded as clear name collisions with a different "Whitaker." A couple of borderline items — a community/policy white paper and an IAU conference proceedings entry, both with genuine Whitaker co-authorship — were deliberately left out pending her call on whether to count them. The h-index/citation totals in the header line are still the November 2025 snapshot — a live ADS API pull would be needed to refresh those two numbers specifically.
- **News: all 32 posts are mirrored locally**, including the two oldest (2017–2018) that were originally missing.
- **Four previously-missing standalone pages are now mirrored locally**: `astronomy-research-tutorial-repository.html`, `data-products.html`, `graduate-student-research-agreement.html`, and `data-challenge.html` (none of these have their own nav-bar tab, matching the original site; they're linked from Research, Teaching, Outreach, and Mentoring Resources same as before). All of the individual downloadable resource files these pages (plus `outreach.html`) link to — 22 undergraduate tutorial PDFs/notebooks/data files in `assets/docs/tutorials/`, the 2 Eureka Workshop worksheets in `assets/docs/outreach/`, the Graduate Student Research Agreement PDF, and the 3D-Herschel README + Caliendo compilation CSV in `assets/docs/data-products/` — were supplied directly by the user and are now hosted locally rather than linking out to astrowhit.com/s/.
- **No CMS, search, comments, or contact form.** The original Squarespace site has a `/search` page, a commenting system on news posts, and various Squarespace-specific interactive blocks (image galleries with lightboxes, "View fullsize" overlays, etc.). None of that dynamic functionality exists here — image galleries are simple flexbox grids of `<img>` tags, and there is no search or comment functionality.
- **Visual design does not match Squarespace.** As specified in the build brief, this uses a clean, original academic-style layout (serif headings, generous whitespace, responsive CSS in `assets/css/style.css`) rather than trying to pixel-match the Squarespace template, which is expected to change anyway.
- **Some homepage banner images were skipped.** A handful of images referenced in the original build brief (`banner_uncover.png`, `16635409814_684de15b6b_o.jpg`, `IMG_5247.JPG`, `Whitaker_eclipse.jpg`, `Whitaker_DAWN22.jpeg`, `IMG_2872_crop.jpg`) did not have confirmed source URLs available and were intentionally left out of the homepage image strip rather than guessed.

## Content accuracy

Every fact, name, date, and publication detail reproduced here was taken directly from the live astrowhit.com pages (or, where noted above, deliberately left out rather than invented). If you spot anything that has since changed on the live site, please update the corresponding HTML file directly — there's no database or CMS to sync from.
