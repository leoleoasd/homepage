#!/usr/bin/env python3
"""Compact horizontal bar chart: types of study-design edits UX researchers made
after using UXAgent. Sits on the right half of a slide next to a big "14/16".

Polished monochrome chart for a Metropolis/moloch beamer slide, matching the
Helvetica typography and label treatment of post_study_ratings.py. Renders both
a vector PDF (for the slide) and a PNG (visual check).
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

# --------------------------------------------------------------------------- #
#  SHARED STYLE  (kept identical across both deck figures)                     #
# --------------------------------------------------------------------------- #
def apply_style():
    """Register Helvetica from the macOS system and set a clean rcParams base.

    Returns the resolved font family name so callers can confirm it loaded a
    /System path rather than the DejaVu fallback.
    """
    family = "Helvetica"
    for path in (
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/HelveticaNeue.ttc",
    ):
        try:
            font_manager.fontManager.addfont(path)
            family = "Helvetica" if path.endswith("Helvetica.ttc") else "Helvetica Neue"
            break
        except Exception:
            continue
    resolved = font_manager.findfont(family, fallback_to_default=False)
    if "/System/Library" not in resolved:
        font_manager.fontManager.addfont("/System/Library/Fonts/HelveticaNeue.ttc")
        family = "Helvetica Neue"
        resolved = font_manager.findfont(family, fallback_to_default=False)

    plt.rcParams.update(
        {
            "font.family": family,
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "axes.unicode_minus": True,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
        }
    )
    return family, resolved


STYLE = {
    "bar": "#1F1F1F",        # refined near-black
    "red": "#C0392B",        # single accent (unused here, kept for parity)
    "ytick": "#1F1F1F",      # category labels
    "label_pt": 13,          # value labels
    "ytick_pt": 12.5,        # category labels
    "bar_h": 0.6,            # ~0.6 of category step
}

SEMIBOLD = 600  # numeric equivalent of "semibold" across matplotlib builds

# --------------------------------------------------------------------------- #
#  DATA                                                                        #
# --------------------------------------------------------------------------- #
# DESCENDING count (top -> bottom). barh draws the first list entry at the
# bottom, so we reverse for plotting.
items = [
    ("Tasks", 6),
    ("Demographics", 3),
    ("Survey items", 2),
    ("Interview protocol", 2),
    ("Added metrics", 2),
]

labels = [it[0] for it in items][::-1]
counts = [it[1] for it in items][::-1]


def main():
    family, resolved = apply_style()
    print("font family:", family)
    print("findfont:", resolved)

    y = list(range(len(labels)))

    fig, ax = plt.subplots(figsize=(5.6, 2.8), dpi=200)

    ax.barh(y, counts, height=STYLE["bar_h"], color=STYLE["bar"],
            linewidth=0, zorder=3)

    # Integer value labels just outside each bar tip.
    for yi, c in zip(y, counts):
        ax.text(c + 0.12, yi, str(c), va="center", ha="left",
                fontsize=STYLE["label_pt"], fontweight=SEMIBOLD,
                color=STYLE["bar"])

    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=STYLE["ytick_pt"], color=STYLE["ytick"])

    # Hide the x-axis entirely (counts are labeled), no gridlines.
    ax.set_xlim(0, max(counts) + 0.85)
    ax.set_ylim(-0.7, len(labels) - 0.3)
    ax.set_xticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis="x", length=0)
    ax.tick_params(axis="y", length=0, pad=8)

    out_pdf = "figures/uxagent/protocol_edits.pdf"
    out_png = "figures/uxagent/protocol_edits.png"
    fig.savefig(out_pdf, bbox_inches="tight", pad_inches=0.15, facecolor="white")
    fig.savefig(out_png, bbox_inches="tight", pad_inches=0.15, facecolor="white",
                dpi=200)
    print("wrote", out_pdf)
    print("wrote", out_png)


if __name__ == "__main__":
    main()
