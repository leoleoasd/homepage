#!/usr/bin/env python3
"""Diverging Likert bar chart of post-study ratings (N=16 UX researchers).

Polished monochrome + single red-accent chart for a Metropolis/moloch beamer
slide (Helvetica typography to match the deck's tgheros). Outputs a vector PDF
for the slide and a PNG for visual checking.
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
        # Helvetica truly unavailable; fall back to Helvetica Neue explicitly.
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
    "red": "#C0392B",        # single accent
    "err": "#B5B5B5",        # elegant error bars
    "zero": "#CBCBCB",       # zero reference line
    "tick": "#9A9A9A",       # light axis ticks
    "ytick": "#1F1F1F",      # category labels
    "hint": "#9A9A9A",       # disagree/agree + N hints
    "label_pt": 13,          # value labels
    "ytick_pt": 12.5,        # category labels
    "bar_h": 0.6,            # ~0.6 of category step
}

# "semibold" isn't a named weight in every matplotlib build; 600 is the numeric
# equivalent and renders the Helvetica semibold-ish weight reliably.
SEMIBOLD = 600


def fmt(v):
    """Format a value with a real Unicode minus sign (U+2212) for negatives."""
    return f"{v:.2f}".replace("-", "−")


# --------------------------------------------------------------------------- #
#  DATA                                                                        #
# --------------------------------------------------------------------------- #
# Items in DESCENDING mean (top -> bottom). barh draws the first list entry at
# the bottom, so we reverse for plotting.
items = [
    ("Usability", 1.63, 0.50),
    ("Helpfulness", 1.38, 0.72),
    ("Satisfaction (revised protocol)", 1.00, 0.89),
    ("Trust", 0.63, 0.81),
    ('“LLM can replace humans”', -0.44, 1.15),
]

labels = [it[0] for it in items][::-1]
means = [it[1] for it in items][::-1]
sds = [it[2] for it in items][::-1]


def main():
    family, resolved = apply_style()
    print("font family:", family)
    print("findfont:", resolved)

    bar_colors = [STYLE["red"] if m < 0 else STYLE["bar"] for m in means]
    y = list(range(len(labels)))

    fig, ax = plt.subplots(figsize=(8.5, 3.4), dpi=200)

    # Zero reference line (behind bars).
    ax.axvline(0, color=STYLE["zero"], lw=1.3, zorder=1)

    # Bars.
    ax.barh(y, means, height=STYLE["bar_h"], color=bar_colors,
            linewidth=0, zorder=3)

    # Elegant +/- SD error bars (above bars).
    ax.errorbar(means, y, xerr=sds, fmt="none", ecolor=STYLE["err"],
                elinewidth=1.3, capsize=3, capthick=1.3, zorder=5)

    # Value labels just outside each bar tip (color matches the bar).
    pad = 0.08
    for yi, m in zip(y, means):
        if m >= 0:
            x = m + sds[yi] + pad
            ha, col = "left", STYLE["bar"]
        else:
            x = m - sds[yi] - pad
            ha, col = "right", STYLE["red"]
        ax.text(x, yi, fmt(m), va="center", ha=ha,
                fontsize=STYLE["label_pt"], fontweight=SEMIBOLD, color=col)

    # Axis extents & ticks.
    ax.set_xlim(-2.45, 2.55)
    ax.set_xticks([-2, -1, 0, 1, 2])
    ax.set_xticklabels(["−2", "−1", "0", "1", "2"],
                       fontsize=10.5, color=STYLE["tick"])
    ax.set_ylim(-0.7, len(labels) - 0.3)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=STYLE["ytick_pt"], color=STYLE["ytick"])

    # Subtle disagree / agree hints under the scale ends (italic, light grey),
    # placed below the tick numbers in axes coords so they never collide.
    ax.text(-2, -0.13, "disagree", transform=ax.get_xaxis_transform(),
            ha="center", va="top", fontsize=9.5, style="italic",
            color=STYLE["hint"])
    ax.text(2, -0.13, "agree", transform=ax.get_xaxis_transform(),
            ha="center", va="top", fontsize=9.5, style="italic",
            color=STYLE["hint"])

    # Unobtrusive N in the upper-right.
    ax.text(0.998, 1.0, "N = 16", transform=ax.transAxes, ha="right",
            va="top", fontsize=10, color=STYLE["hint"])

    # Spines: hide top/right/left; keep a very light bottom axis.
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color("#E2E2E2")
    ax.spines["bottom"].set_linewidth(0.9)
    ax.tick_params(axis="x", length=3, color="#E2E2E2", pad=4)
    ax.tick_params(axis="y", length=0, pad=8)

    out_pdf = "figures/uxagent/post_study_ratings.pdf"
    out_png = "figures/uxagent/post_study_ratings.png"
    fig.savefig(out_pdf, bbox_inches="tight", pad_inches=0.15, facecolor="white")
    fig.savefig(out_png, bbox_inches="tight", pad_inches=0.15, facecolor="white",
                dpi=200)
    print("wrote", out_pdf)
    print("wrote", out_png)


if __name__ == "__main__":
    main()
