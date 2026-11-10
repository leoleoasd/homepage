# AGENTS.md — `files/talks/3_papers`

## Project overview

This is **not a software project** — there is no `pyproject.toml`, `package.json`, `Makefile`, test suite, or CI. It is a directory of **LaTeX slides and paper sources** for the academic talks of Yuxuan Lu (Northeastern University), living inside the personal-homepage repo `github.com/leoleoasd/homepage` at `files/talks/3_papers/`. The final artifacts are PDF slide decks; the compiled PDFs **are committed to git** alongside the sources.

There are two kinds of `.tex` files here:

### Beamer slide decks (the primary, buildable content)

- `talk.tex` — deck "Human–AI Collaboration for UX Research" (Mar 2026) → `talk.pdf`.
- `user-simulator.tex` — deck "Designing, Evaluating, and Improving LLM Agents as Simulated Users" (Jun 2026) → `user-simulator.pdf`. This is the newer, expanded version of the same talk (Introduction → Case Study 1: UXAgent → Case Study 2: Agent A/B → Case Study 3: multi-turn behavior → WebServ).
- `agentab.tex` — **frames-only fragment, no preamble**. It is shared: `\input{agentab}` is used by both `user-simulator.tex` and `agentab_preview.tex`. Never build it directly; edit it once and both decks pick it up.
- `agentab_preview.tex` — small standalone deck that wraps `agentab.tex` for iterating on the Case Study 2 (Agent A/B) slides quickly → `agentab_preview.pdf`.
- `human-ai-collab.tex` — near-duplicate working variant of `talk.tex` (same title/date, ~27 differing lines), currently **untracked in git** and with no committed PDF. Treat `talk.tex` as canonical.

### Paper sources kept for reference (not standalone-buildable here)

- `uxagent.tex` (ACM `acmart`), `finetuned.tex` and `webserv.tex` (ACL style), `webserv_rebuttal.md`.
- These are copies used to pull content into slides. They **do not compile in this directory**: `webserv.tex`/`finetuned.tex` need `acl.sty`, and `uxagent.tex` needs `set.bib`/`newRef.bib` — none of which are here. Canonical buildable copies live in the sibling directories `files/talks/{uxagent,webserv,finetuned_web_agent}/`.

### Shared assets

- `yuxuan.bib`, `custom.bib` — both are `\addbibresource`'d together by every deck. Add new references to one of these.
- `figures/` — image assets by relative path (`figures/<name>.png|pdf`). Per-paper subdirectories: `figures/agentab/`, `figures/uxagent/`, `figures/finetuned_web_agent/`, `figures/webserv/`. `figures/uxagent/protocol_edits.py` and `post_study_ratings.py` are small matplotlib scripts that regenerate the corresponding PDF/PNG charts.
- `_minted/`, `_minted-talk/` — minted (Pygments) cache directories; generated, safe to delete.

## Build commands

Toolchain: TeX Live 2025 (`/Library/TeX/texbin`), `latexmk` + `pdflatex` + `biber`, Pygments (`pygmentize`, via `micromamba`), and the **moloch** beamer theme installed in the user tree (`~/Library/texmf/tex/latex/moloch/`). Build a deck:

```bash
latexmk talk.tex              # or user-simulator.tex / agentab_preview.tex
```

latexmk runs the full `pdflatex → biber → pdflatex × 2` cycle automatically. Notes:

- **`-shell-escape` is required** because the decks use `minted` for code listings. The VS Code LaTeX Workshop magic comment `%!LW recipe=pdfLaTeXmk` at the top of each deck selects the project's configured recipe; if you invoke tools manually, use `latexmk -pdflatex='pdflatex -shell-escape -interaction=nonstopmode' <file>` or equivalent.
- Bibliographies use **biblatex with the biber backend** (not bibtex) for the decks.
- There is **no `.latexmkrc`** — configuration is the LaTeX Workshop recipe plus magic comments.

## Code style / conventions

When editing or adding slides, follow the existing idioms rather than inventing new ones:

- **Shared preamble pattern.** All decks carry an identical preamble block (16:9 `beamer` with `[scheme=plain,aspectratio=169]`, moloch theme, the same package list, the `\silentfootcite`/`\silentfootcitetext` biblatex machinery, `\imageframe`, and color definitions — see `talk.tex:1-190`). New decks should copy this block verbatim and adjust only title/author/date.
- **Citations**: `\cite` is renewed to `\footcite`; references render as tiny footnotes in authoryear style. Use `\silentfootcite{key}` for a marker-free footnote citation. Bib keys come from `yuxuan.bib` / `custom.bib`.
- **Full-bleed figures**: use the custom `\imageframe{figures/foo.png}[scale]` command (scale optional, default 1). Section-transition slides use `\begin{frame}[standout]`.
- **'Todo' marker**: `\todo{...}` highlights unfinished text in red for in-deck reminders.
- **Tables**: `tabularray` (`tblr`); **colors**: `ninecolors` scale names (e.g. `gray1`) plus custom `ForestGreen`; icons via `fontawesome5`/`academicons`; QR codes via `qrcode`.
- Figures are referenced by relative path; keep new assets under `figures/` (per-paper subdirectory when applicable). Generated charts belong next to their generating script (see `figures/uxagent/`).
- Beamer decks are self-contained per top-level file except for `\input` fragments (`agentab.tex`); fragments must contain frames only.

## Testing / verification

There are no automated tests. Verification is:

1. `latexmk <deck>.tex` exits 0.
2. Check the `.log`/terminal for `LaTeX Warning: Citation ... undefined` / `There were undefined references` (usually means biber didn't rerun or a bib key is missing).
3. Visually inspect the resulting PDF (figure paths, frame overflow, footnote citations).
4. If you edited matplotlib chart scripts in `figures/uxagent/`, rerun the script and re-check the regenerated PDF/PNG before rebuilding the deck.

## Repository & git conventions

- Part of the `homepage` git repo. Tracked here: `*.tex` sources, `*.bib`, `webserv_rebuttal.md`, `figures/`, and the final PDFs (`talk.pdf`, `user-simulator.pdf`, `agentab_preview.pdf`). All intermediate build artifacts (`.aux`, `.bbl`, `.fdb_latexmk`, `.fls`, `.log`, `.nav`, `.out`, `.run.xml`, `.snm`, `.synctex.gz`, `.toc`, `_minted*/`) are git-ignored — don't worry about them, but also never hand-edit generated files like `.bbl`.
- The PDFs are large binaries (up to ~26 MB) committed to the repo; rebuilding and committing them is the normal workflow.
- The repo-root `AGENTS.md` (at `/Volumes/Code/homepage/AGENTS.md`) defines a merge policy: never overwrite or revert user-made/external changes; merge around existing content.

## Security considerations

Nothing sensitive here: the content is public academic material. Two operational cautions apply:

- `minted` requires `-shell-escape`, which lets LaTeX execute shell commands during compilation — only compile sources you trust.
- Do not run `latexmk -C` carelessly: unlike `-c` (safe, removes only aux files), `-C` also deletes the generated PDFs, which are committed deliverables.
