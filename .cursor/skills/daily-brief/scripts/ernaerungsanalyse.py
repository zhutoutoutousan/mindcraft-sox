#!/usr/bin/env python3
"""Generate crisp charts + German LaTeX nutrition/weight analysis PDF sources in tmp/."""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

def _tmp() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "CPU.md").is_file():
            d = parent / "tmp"
            d.mkdir(exist_ok=True)
            return d
    return Path(__file__).resolve().parent

ROOT = _tmp()
DPI = 300

# Colors aligned with daily-brief template (no purple/cream AI defaults)
INK = "#1A1A1A"
MUTED = "#5C5C5C"
ACCENT = "#1F4E3D"
LINK = "#1F4E79"
YES = "#2E6B4F"
WARN = "#A65D3B"
MID = "#C4A35A"


def style_ax(ax) -> None:
    ax.set_facecolor("#F7F4EE")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(MUTED)
    ax.spines["bottom"].set_color(MUTED)
    ax.tick_params(colors=MUTED, labelsize=9)
    ax.yaxis.label.set_color(INK)
    ax.xaxis.label.set_color(INK)
    ax.title.set_color(INK)


def chart_weight() -> Path:
    dates = ["09.10.", "11.10.", "14.10."]
    kg = [66.05, 66.70, 65.85]
    fig, ax = plt.subplots(figsize=(7.2, 3.6), dpi=DPI)
    style_ax(ax)
    fig.patch.set_facecolor("#F7F4EE")
    ax.plot(dates, kg, color=ACCENT, marker="o", linewidth=2.4, markersize=8, zorder=3)
    ax.fill_between(dates, kg, min(kg) - 0.15, color=ACCENT, alpha=0.12)
    for d, v in zip(dates, kg):
        ax.annotate(
            f"{v:.2f} kg",
            (d, v),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
            fontsize=9,
            color=INK,
        )
    ax.axhline(65.85, color=LINK, linestyle="--", linewidth=1, alpha=0.5)
    ax.set_ylabel("Körpergewicht (kg)")
    ax.set_title("Gewichtstrend (Morgen-Messungen)")
    ax.set_ylim(65.5, 67.0)
    ax.grid(axis="y", color="#D9D4C8", linewidth=0.6)
    out = ROOT / "fig-gewicht.pdf"
    fig.tight_layout()
    fig.savefig(out, format="pdf", bbox_inches="tight")
    plt.close(fig)
    return out


def chart_calories() -> Path:
    dates = ["09.10.", "10.10.", "11.10.", "12.10."]
    intake = [1305, 1975, 1881, 1442]
    tdee = [2099, 2099, 2336, 2099]
    x = range(len(dates))
    fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=DPI)
    style_ax(ax)
    fig.patch.set_facecolor("#F7F4EE")
    w = 0.36
    ax.bar([i - w / 2 for i in x], intake, width=w, color=ACCENT, label="Zufuhr")
    ax.bar([i + w / 2 for i in x], tdee, width=w, color=LINK, alpha=0.75, label="TDEE")
    for i, (a, b) in enumerate(zip(intake, tdee)):
        delta = a - b
        ax.annotate(
            f"{delta:+d}",
            (i, max(a, b) + 40),
            ha="center",
            fontsize=8,
            color=YES if delta < 0 else WARN,
        )
    ax.set_xticks(list(x))
    ax.set_xticklabels(dates)
    ax.set_ylabel("kcal / Tag")
    ax.set_title("Kalorienzufuhr vs. Tagesumsatz (vollständige Tage)")
    ax.legend(frameon=False, fontsize=9)
    ax.grid(axis="y", color="#D9D4C8", linewidth=0.6)
    out = ROOT / "fig-kalorien.pdf"
    fig.tight_layout()
    fig.savefig(out, format="pdf", bbox_inches="tight")
    plt.close(fig)
    return out


def chart_protein() -> Path:
    dates = ["09.10.", "10.10.", "11.10.", "12.10.", "13.10.*"]
    protein = [92, 119, 105, 54, 61]
    per_kg = [1.39, 1.78, 1.57, 0.81, 0.91]
    fig, ax1 = plt.subplots(figsize=(7.2, 3.8), dpi=DPI)
    style_ax(ax1)
    fig.patch.set_facecolor("#F7F4EE")
    colors = [YES if p >= 80 else WARN for p in protein]
    bars = ax1.bar(dates, protein, color=colors, width=0.55)
    ax1.axhline(80, color=LINK, linestyle="--", linewidth=1.2, label="Ziel ≈ 80 g")
    ax1.set_ylabel("Protein (g)")
    ax1.set_title("Proteinzufuhr (13.10. nur Brunch erfasst)")
    ax2 = ax1.twinx()
    ax2.plot(dates, per_kg, color=MID, marker="s", linewidth=1.8, label="g/kg")
    ax2.set_ylabel("g / kg Körpergewicht", color=MUTED)
    ax2.tick_params(axis="y", colors=MUTED)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_color(MUTED)
    ax1.legend(loc="upper left", frameon=False, fontsize=8)
    ax2.legend(loc="upper right", frameon=False, fontsize=8)
    ax1.grid(axis="y", color="#D9D4C8", linewidth=0.6)
    for b, v in zip(bars, protein):
        ax1.annotate(str(v), (b.get_x() + b.get_width() / 2, v + 2), ha="center", fontsize=8, color=INK)
    out = ROOT / "fig-protein.pdf"
    fig.tight_layout()
    fig.savefig(out, format="pdf", bbox_inches="tight")
    plt.close(fig)
    return out


def chart_composition() -> Path:
    # BIA % metrics are overlapping categories — show as bars, not a fake mass pie.
    labels = ["Körperfett\n32.0%", "Unterhautfett\n28.0%", "Skelettmuskel\n36.5%", "Körperwasser\n51.0%"]
    values = [32.0, 28.0, 36.5, 51.0]
    colors = [WARN, MID, ACCENT, LINK]
    fig, ax = plt.subplots(figsize=(6.4, 4.0), dpi=DPI)
    style_ax(ax)
    fig.patch.set_facecolor("#F7F4EE")
    bars = ax.barh(labels, values, color=colors, height=0.62)
    ax.set_xlim(0, 60)
    ax.set_xlabel("% (BIA, überlappende Kennzahlen)")
    ax.set_title("Körperzusammensetzung 14.10. · Score 90/100")
    for b, v in zip(bars, values):
        ax.annotate(f"{v:.1f}", (v + 0.6, b.get_y() + b.get_height() / 2), va="center", fontsize=9, color=INK)
    ax.grid(axis="x", color="#D9D4C8", linewidth=0.6)
    out = ROOT / "fig-koerper.pdf"
    fig.tight_layout()
    fig.savefig(out, format="pdf", bbox_inches="tight")
    plt.close(fig)
    return out


def chart_activity() -> Path:
    labels = ["30.09.\nSchritte", "11.10.\nAusflug", "12.–14.10.\nKraft"]
    values = [9765, 1, 0]  # qualitative: steps, outing flag, strength sessions logged
    fig, ax = plt.subplots(figsize=(7.2, 3.4), dpi=DPI)
    style_ax(ax)
    fig.patch.set_facecolor("#F7F4EE")
    # Dual display: steps as bar + note for others via text panel style
    ax.bar(["30.09."], [9765], color=ACCENT, width=0.45)
    ax.set_ylabel("Schritte")
    ax.set_title("Aktivität (erfasst): Schritte · Ausflug · Kraft (nicht gemeldet)")
    ax.set_ylim(0, 12000)
    ax.axhline(10000, color=LINK, linestyle="--", linewidth=1, alpha=0.7)
    ax.annotate("WHO ≈ 10.000", (0, 10000), xytext=(0.35, 10500), fontsize=8, color=LINK)
    ax.text(
        0.62,
        0.55,
        "11.10.: langer Spaziergang/Ausflug\n→ TDEE-Faktor sehr aktiv (1.725)\n\n"
        "Krafttraining: self/training.toon.md\nfehlt → Gruppen nicht gemeldet",
        transform=ax.transAxes,
        fontsize=8.5,
        color=INK,
        va="center",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="#D9D4C8"),
    )
    ax.grid(axis="y", color="#D9D4C8", linewidth=0.6)
    out = ROOT / "fig-aktivitaet.pdf"
    fig.tight_layout()
    fig.savefig(out, format="pdf", bbox_inches="tight")
    plt.close(fig)
    return out


def write_tex() -> Path:
    tex = ROOT / "day-2026-10-14.tex"
    tex.write_text(
        r"""% Nutrition / weight / activity analysis — German body. Generated into tmp/.
\documentclass[11pt,a4paper]{ctexart}
\usepackage[margin=1.6cm,top=1.65cm,bottom=1.8cm]{geometry}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,fit,calc}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{colortbl}
\usepackage{array}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage{microtype}

\hypersetup{colorlinks=true,urlcolor=linkb,pdftitle={Ernaehrungs- und Gewichtsanalyse 2026-10-14}}

\definecolor{ink}{HTML}{1A1A1A}
\definecolor{muted}{HTML}{5C5C5C}
\definecolor{accent}{HTML}{1F4E3D}
\definecolor{linkb}{HTML}{1F4E79}
\definecolor{paper}{HTML}{F7F4EE}
\definecolor{yes}{HTML}{E8F0EA}
\definecolor{no}{HTML}{F6E8E6}
\definecolor{mid}{HTML}{F7F0E4}
\definecolor{unk}{HTML}{E8E6E1}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.3pt}
\fancyhead[L]{\small\color{muted}Europe/Berlin}
\fancyhead[R]{\small\color{accent}Analyse Gewicht · Nahrung · Sport}
\fancyfoot[L]{\small\color{muted}tmp/day-2026-10-14.pdf}
\fancyfoot[R]{\small\color{muted}\thepage}

\setlist[itemize]{leftmargin=1.15em,itemsep=0.08em,topsep=0.1em}
\setlength{\parskip}{0.18em}
\setlength{\parindent}{0pt}
\setcounter{secnumdepth}{0}

\newcommand{\blocktable}[1]{%
\par
{\footnotesize
\noindent
\begin{tabularx}{\linewidth}{@{}
  >{\raggedright\arraybackslash}p{0.26\linewidth}
  >{\raggedright\arraybackslash}X
  >{\raggedright\arraybackslash}p{0.22\linewidth}@{}}
#1
\end{tabularx}}%
\par
}

\begin{document}
\pagecolor{paper}
\color{ink}

{\LARGE\bfseries\color{accent} Zusammenfassung \& Analyse}\\[0.15em]
{\large Gewicht · Ernährung · Aktivität · 09.--14.10.2026}\\[0.35em]
{\small\color{muted}Quellen: \texttt{self/nutrition.toon.md}. Kraftgruppen: nicht gemeldet (kein \texttt{training.toon.md}). Schätzungen $\pm$10--15\,\%.}

\section{Status heute (14.10., Morgen)}
\par
\blocktable{
\toprule
\textbf{Feld} & \textbf{Wert} & \textbf{Hinweis} \\
\midrule
\rowcolor{yes} Körpergewicht & 65{,}85\,kg & $-$0{,}85\,kg seit 11.10.; $-$0{,}20\,kg seit 09.10. \\
BMI & 23{,}3 & Normalbereich (18{,}5--24{,}9) \\
Körperfett (BIA) & 32{,}0\,\% & leicht erhöht; $-$0{,}9\,pp seit 09.10. \\
Muskelmasse & 44{,}8\,kg / 36{,}5\,\% Skelettmuskel & Standard \\
BMR (App) & 1306\,kcal/Tag & Mifflin $\approx$ 1348\,kcal \\
Score & 90/100 & visz. Fett Level 5 (gesund) \\
\bottomrule
}

\noindent\begin{minipage}[t]{0.52\linewidth}
\includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{fig-gewicht.pdf}
\end{minipage}\hfill
\begin{minipage}[t]{0.46\linewidth}
\includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{fig-koerper.pdf}
\end{minipage}

{\small\color{muted}11.10.\ +0{,}65\,kg nach spätem Essen am 10.10.\ = Wassereinlagerung/voller Magen, kein Fettaufbau (kein $\approx$5000+\,kcal-Überschuss).}

\section{Kalorien · Protein}
\par
\noindent\begin{minipage}[t]{0.49\linewidth}
\includegraphics[width=\linewidth,height=0.34\textheight,keepaspectratio]{fig-kalorien.pdf}
\end{minipage}\hfill
\begin{minipage}[t]{0.49\linewidth}
\includegraphics[width=\linewidth,height=0.34\textheight,keepaspectratio]{fig-protein.pdf}
\end{minipage}

\blocktable{
\toprule
\textbf{Tag} & \textbf{Zufuhr / TDEE / Bilanz} & \textbf{Kurzfasung} \\
\midrule
09.10. & 1305 / 2099 / $-$794 & starkes Defizit, Protein gut \\
\rowcolor{mid} 10.10. & 1975 / 2099 / $-$124 & fast Erhalt; späte Mahlzeit \\
11.10. & 1881 / 2336 / $-$455 & Ausflug; Marzipan-Snack hoch \\
\rowcolor{yes} 12.10. & 1442 / 2099 / $-$657 & großes Defizit; Protein zu niedrig \\
13.10. & 865+ (unvollständig) / --- & nur Brunch geloggt \\
\bottomrule
}

{\small Mittel 09.--12.10.: $\approx$86\,g Protein/Tag ($\approx$1{,}29\,g/kg). Warnung 12.10.: nur $\approx$54\,g --- vegetarische Bowl ohne Proteinquelle. Ziel: 80--100\,g/Tag.}

\section{Sport · Nordkette · LOAD 1}
\par
\noindent\begin{minipage}[t]{0.55\linewidth}
\includegraphics[width=\linewidth,height=0.30\textheight,keepaspectratio]{fig-aktivitaet.pdf}
\end{minipage}\hfill
\begin{minipage}[t]{0.42\linewidth}
\begin{center}
\begin{tikzpicture}[
  node distance=0.4cm and 0.45cm,
  box/.style={draw=accent, rounded corners=2pt, align=center, font=\scriptsize, inner sep=3pt, fill=yes},
  miss/.style={draw=muted, rounded corners=2pt, align=center, font=\scriptsize, inner sep=3pt, fill=unk},
  arr/.style={-{Latex}, thick, accent}
]
\node[box] (w) {Gewicht 65{,}85\,kg};
\node[box, below=of w] (n) {Nahrung geloggt};
\node[miss, below=of n] (s) {Kraft nicht gemeldet};
\node[miss, below=of s] (g) {Ziel im Store offen};
\draw[arr] (w) -- (n);
\draw[arr] (n) -- (s);
\draw[arr] (s) -- (g);
\end{tikzpicture}
\end{center}
\end{minipage}

\blocktable{
\toprule
\textbf{Datum} & \textbf{Erfasst} & \textbf{Bewertung} \\
\midrule
30.09. & 9\,765 Schritte ($\approx$390\,kcal) & nah an 10\,000 \\
\rowcolor{yes} 11.10. & langer Ausflug/Spaziergang & TDEE ``sehr aktiv'' \\
Kraft & nicht gemeldet & keine DOMS-/Satzdaten \\
\bottomrule
}

\begin{enumerate}
  \item Ziel festlegen (Erhalt / Reduktion / Aufbau) --- sonst bleibt der TDEE Rauschen.
  \item Protein-Floor $\ge$80\,g; vegetarische Abende mit Quark/Hülsenfrüchten ergänzen.
  \item Letzte Mahlzeit nicht direkt vor dem Schlafen (siehe 10.$\to$11.10.).
  \item Kraftsätze/DOMS in \texttt{training.toon.md} loggen; 13.10.\ Tag vervollständigen.
\end{enumerate}
{\small\color{muted}Keine Diagnosen. BIA/Portionen $\pm$10--15\,\%. BMI mit Größe 168\,cm.}

\end{document}
""",
        encoding="utf-8",
    )
    return tex


def main() -> None:
    chart_weight()
    chart_calories()
    chart_protein()
    chart_composition()
    chart_activity()
    tex = write_tex()
    print(tex.as_posix())


if __name__ == "__main__":
    main()
