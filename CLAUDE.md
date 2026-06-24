# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Yuxuan Lu's personal academic homepage at https://yuxuan.lu — a Jekyll site forked from the Minimal Mistakes / academicpages template, deployed via GitHub Pages from the `master` branch.

## Common commands

- Local dev server: `bundle exec jekyll liveserve` (rebuilds on change, serves on http://localhost:4000). Use `--config _config.yml,_config.dev.yml` if you need the local-only overrides (`url`, expanded SASS, analytics off).
- One-off build (mirrors CI): `JEKYLL_ENV=production bundle exec jekyll build`. Output goes to `_site/`.
- Ruby deps: `bundle install`. If you hit version errors, delete `Gemfile.lock` and reinstall (see README). CI pins Ruby 3.4.1.
- Update the Google Scholar citation chart: `python scripts/scholar.py` (writes `_data/scholar.json` and regenerates `_includes/scholar.html`). Normally this runs via the `update_scholar.yml` workflow — only run manually if intentionally refreshing locally. Note: the script post-processes the generated `scholar.html` to replace `{{` with `{ {` so Plotly's output doesn't collide with Liquid tag syntax — keep that step if editing the script.

## Merge / edit policy (from AGENTS.md)

Never overwrite or revert user-made/external changes. When updating content, add or adjust minimally around existing material rather than rewriting it. When in doubt, preserve the user's version and add your changes alongside with clear separation.

## Architecture

Standard Jekyll layout with a few project-specific conventions worth knowing before editing:

- **Two bibliographies, two sections.** `_bibliography/references.bib` is rendered as "Publications" and `_bibliography/preprint.bib` as "Preprints" on `_pages/publications.md` via `jekyll-scholar`. When a preprint is accepted to a venue, move the entry from `preprint.bib` → `references.bib`, convert `@misc` → `@inproceedings` (or appropriate type), and set `abbr` to the venue label (e.g. `ACL 2026`, `CHI 2024`, `EMNLP 2023<br>Findings`) — `abbr` is what shows as the badge in the rendered list. Cite keys are referenced from news posts as `#citekey` anchors, so keep keys stable.
- **News collection drives the homepage feed.** Files in `_news/` are dated markdown snippets (frontmatter `date:` + a one-paragraph body). The `news` collection has `output: false` — these are excerpted into the about page, not rendered as standalone pages. News items commonly link to publications via `<a href="#citekey">` anchors that resolve on the publications page.
- **Daily logs are a real collection.** `_daily_log/*` renders with the `daily-log` layout under `/daily_log/:path/`. Distinct from `_posts/` (which uses `single`).
- **Pages live in `_pages/`** and are routed by explicit `permalink` in each file's frontmatter. The `_pages` dir is added via the `include:` list in `_config.yml`.
- **Layouts beyond the template defaults:** `bib.html` (per-entry scholar detail page, configured via `scholar.details_layout`), `daily-log.html`, `talk.html`, `splash.html`. Most page content uses `single`.
- **Data files:** `_data/coauthors.yml`, `venues.yml`, `navigation.yml`, `ui-text.yml` configure cross-cutting content. `_data/scholar.json` is the time series the scholar workflow appends to — do not hand-edit unless fixing bad data.
- **Theme overrides:** SCSS partials in `_sass/`, JS in `assets/js/` (legacy uglify build via `npm run uglify` exists but is rarely needed — the committed `main.min.js` is what ships).
- **Legacy academicpages tooling — usually ignore.** `markdown_generator/` (notebooks/scripts that generate `_publications`/`_talks` markdown from TSV) and `talkmap.py` / `talkmap/` (leaflet map of talk locations) are inherited from the template and not part of the current content workflow — publications come from the `.bib` files, not generated markdown. Don't wire new content through these unless deliberately reviving them.

## Deployment

`.github/workflows/jekyll.yml` builds and deploys to GitHub Pages on every push to `master` and is also called by `update_scholar.yml` after a scholar refresh. There is no staging — pushing to `master` publishes the site.
