# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_b5__bxLYNiMo` — Empirical Audit of Moving Average Baselines in Short-Horizon Time Series Forecasting
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-30 14:35:30 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Empirical Audit of Moving Average Baselines in Short-Horizon Time Series Forecasting
abstract: >-
  Short-horizon time series forecasting in noisy, low-sample regimes presents fundamental trade-offs between noise attenuation
  and lag introduction. While complex recurrent and transformer neural network architectures dominate modern forecasting benchmarks,
  simple classical baselines such as the naive last-value persistence model and moving average smoothing remain foundational.
  In this work, we present a comprehensive empirical audit of moving average forecasting across varying window sizes $K \in
  \{1, 2, 3, 4, 5, 10\}$ and stochastic regimes, addressing reviewer critiques regarding classical baseline generalizability
  and parameter sensitivity. Through rigorous evaluation across 800 synthetic time series trials and Monte Carlo simulations,
  we demonstrate that a 3-point moving average achieves an aggregate Mean Squared Error (MSE) of 1.5399 compared to 1.9094
  for the naive persistence baseline, yielding a statistically significant relative error reduction of 19.35% ($t = 2.316,
  p = 0.0226$). Furthermore, our window sensitivity analysis reveals that while moderate smoothing ($K=3$ to $K=4$) effectively
  dampens additive white noise and AR(1) perturbations, excessively large windows ($K \ge 10$) incur prohibitive phase lag
  penalties. Our findings establish robust performance floors for modern machine learning benchmarking and highlight the critical
  boundaries where classical moving average smoothing outperforms naive persistence.
paper_text: |
  # Introduction

  Short-horizon time series forecasting is a ubiquitous challenge across financial markets, energy grids, operational sensor networks, and supply chain management [1]. In many practical deployment scenarios, time series data are observed over limited temporal windows and contaminated by substantial high-frequency observational noise. A central question confronting practitioners is how to formulate robust baseline forecasts when sample sizes are small and signal-to-noise ratios are low \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-29c492-empirical-audit-of-moving-average-baseli/tree/main/round-1/experiment-1}}.

  Among classical univariate forecasting techniques, the naive last-value forecast (or persistence model) serves as the canonical baseline [2]. By assuming that the future value equals the most recent observation, the naive model requires no parameter estimation and introduces zero phase lag. However, in the presence of additive white noise, persistence forecasting directly extrapolates the most recent noise realization rather than the underlying mean process, leading to severe error amplification \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-29c492-empirical-audit-of-moving-average-baseli/tree/main/round-1/dataset-1}}. To mitigate high-frequency volatility, classical smoothing methods such as moving averages aggregate successive observations to estimate the local level [3].

  [FIGURE:fig1]

  Despite the ubiquity of moving averages in technical analysis and statistical control, rigorous quantitative comparisons against naive persistence under controlled synthetic noise regimes are frequently overlooked in modern machine learning benchmarks, which often jump directly to complex recurrent neural networks or transformer architectures [4]. Understanding the exact performance boundaries between simple smoothing and persistence is essential for establishing rigorous performance floors.

  In this work, we investigate the hypothesis that a 3-point moving average outperforms the naive last-value forecast on short synthetic time series exhibiting stationary means and additive Gaussian noise, and we extend our audit to examine window sensitivity ($K \in \{1, 2, 3, 4, 5, 10\}$) and AR(1) serial correlation regimes \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-29c492-empirical-audit-of-moving-average-baseli/tree/main/round-2/dataset-1}}. Utilizing 800 independent Monte Carlo trials across multiple noise variance levels ($\sigma \in \{0.5, 1.0, 2.0\}$), we evaluate both forecasting strategies under identical conditions \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-29c492-empirical-audit-of-moving-average-baseli/tree/main/round-2/experiment-1}}. Our results demonstrate that the 3-point moving average achieves a mean squared error (MSE) reduction of 31.08% relative to the naive baseline in pure white noise ($t = 8.83, p < 1e-17$) \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-29c492-empirical-audit-of-moving-average-baseli/tree/main/round-1/evaluation-1}}, and an aggregate MSE of 1.5399 versus 1.9094 ($t = 2.316, p = 0.0226$) across stochastic evaluations \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-29c492-empirical-audit-of-moving-average-baseli/tree/main/round-2/evaluation-1}}.

  Our key contributions are summarized as follows:
  - We formulate a controlled empirical evaluation framework comparing moving average smoothing against naive persistence across 800 synthetic time series trials .
  - We audit window size sensitivity across $K \in \{1, 2, 3, 4, 5, 10\}$, quantifying the exact trade-off between variance attenuation and lag introduction .
  - We extend the evaluation to AR(1) stochastic processes, establishing robust performance floors and identifying break-even boundaries for classical smoothing baselines .

  # Related Work

  Univariate time series forecasting has a rich history rooted in classical statistical literature [1]. The foundational frameworks established by Box and Jenkins [1] formalized autoregressive integrated moving average (ARIMA) models, demonstrating how moving average components capture short-term dependencies and smooth stochastic perturbations. Similarly, exponential smoothing and simple moving averages have long served as bedrock techniques in industrial inventory control and economic forecasting [2].

  In modern forecasting literature, empirical evaluations regularly benchmark sophisticated machine learning models against classical statistical baselines. Large-scale forecasting competitions such as the M-competitions (e.g., M4 and M5) have repeatedly highlighted that well-tuned classical statistical methods and simple combination baselines frequently match or exceed complex deep learning architectures on noisy, irregular time series [3]. Botchkarev [4] provides a comprehensive taxonomy of regression and forecasting error measures, emphasizing the critical importance of utilizing Mean Squared Error (MSE) and Mean Absolute Error (MAE) under appropriate distributional assumptions.

  Despite the prevalence of advanced neural architectures, understanding the fundamental mechanics of baseline smoothing versus persistence in micro-scale horizons remains vital. Our work bridges this gap by positioning itself as an empirical baseline audit and performance floor study for modern time series research, addressing reviewer critiques regarding classical baseline generalizability .

  # Methodology

  We consider a univariate stationary time series process where each observed value $X_t$ consists of an underlying stationary mean $\mu$ perturbed by additive Gaussian white noise:

  $$X_t = \mu + \epsilon_t, \quad \text{where } \epsilon_t \sim \mathcal{N}(0, \sigma^2)$$

  To address reviewer feedback regarding serial correlation, we also evaluate AR(1) processes where observations follow:

  $$X_t = c + \phi X_{t-1} + \epsilon_t$$

  Given a discrete sequence of observations up to time $T$, our objective is to forecast the future value $X_{T+1}$. We evaluate two competing forecasting families:

  ## Naive Last-Value Forecast
  The naive forecasting model assumes persistence of the most recent observation :

  $$\hat{X}_{T+1}^{\text{naive}} = X_T = \mu + \epsilon_T$$

  The expected squared error for the naive forecast under white noise is:

  $$\mathbb{E}\left[ (X_{T+1} - \hat{X}_{T+1}^{\text{naive}})^2 \right] = \mathbb{E}\left[ (\epsilon_{T+1} - \epsilon_T)^2 \right] = 2 \sigma^2$$

  ## Rolling Moving Average Forecast
  The $K$-point moving average computes the arithmetic mean of the $K$ most recent observations to estimate the local level :

  $$\hat{X}_{T+1}^{\text{MA}(K)} = \frac{1}{K} \sum_{i=0}^{K-1} X_{T-i} = \mu + \frac{1}{K} \sum_{i=0}^{K-1} \epsilon_{T-i}$$

  Assuming independence of noise terms across time steps, the expected squared error for the 3-point moving average ($K=3$) is:

  $$\mathbb{E}\left[ (X_{T+1} - \hat{X}_{T+1}^{\text{MA}(3)})^2 \right] = \left(1 + \frac{1}{9} + \frac{1}{9} + \frac{1}{9}\right) \sigma^2 = \frac{4}{3} \sigma^2 \approx 1.333 \sigma^2$$

  Comparing theoretical mean squared errors, the ratio of the moving average MSE to the naive MSE is $(4/3) / 2 = 2/3 \approx 0.667$, implying a theoretical error reduction of approximately 33.3% in asymptotic stationary regimes .

  [FIGURE:fig2]

  # Experiments and Results

  To empirically validate our theoretical derivation and address reviewer critiques regarding parameter sensitivity and AR(1) processes, we construct a synthetic dataset comprising 800 time series trials  evaluated across rolling window sizes $K \in \{1, 2, 3, 4, 5, 10\}$ .

  Table 1 summarizes the empirical Mean Squared Error (MSE) results for the 3-point moving average versus the naive baseline across noise standard deviation levels .

  | Noise Level ($\sigma$) | Naive MSE | Moving Average (3-Pt) MSE | MSE Reduction (\%) | $p$-value |
  | :--- | :--- | :--- | :--- | :--- |
  | $\sigma = 0.5$ | 0.4856 | 0.3347 | 31.08\% | $< 1e-17$ |
  | $\sigma = 1.0$ | 1.9426 | 1.3389 | 31.08\% | $< 1e-17$ |
  | $\sigma = 2.0$ | 7.7702 | 5.3556 | 31.08\% | $< 1e-17$ |
  | **Aggregated (Pure Noise)** | **1.9426** | **1.3389** | **31.08\%** | **$< 1e-17$** |

  Furthermore, across our comprehensive stochastic evaluation incorporating AR(1) dynamics and window sensitivity across 100 trials, the aggregate moving average performance yields an MSE of 1.5399 compared to 1.9094 for naive persistence, representing a relative error reduction of 19.35\% ($t = 2.316, p = 0.0226$) .

  [FIGURE:fig3]

  As detailed in Figure 3, our window sensitivity audit across $K \in \{1, 2, 3, 4, 5, 10\}$ reveals a clear U-shaped error curve. While $K=1$ is identical to naive persistence (MSE 1.9094), smoothing windows $K=3$ and $K=4$ achieve optimal noise attenuation. Conversely, expanding the window to $K=10$ results in oversmoothing and lag penalties that degrade forecasting accuracy .

  # Discussion

  Our empirical findings demonstrate that simple temporal smoothing robustly outperforms persistence in stationary noisy time series. While the naive model avoids introducing lag, its susceptibility to instantaneous noise realization dominates the error profile. By averaging over multiple time steps, the moving average dampens noise variance.

  However, these findings must be contextualized within certain methodological limitations:
  1. **Stationarity and AR(1) Bounds**: While additive white noise benefits substantially from moving averages, strong positive serial correlation ($\phi \ge 0.8$) shifts the optimal strategy back toward persistence or adaptive smoothing to avoid lag.
  2. **Fixed vs. Adaptive Window Hyperparameters**: Although $K=3$ provides an effective default for short horizons ($T \le 100$), dynamic environments require adaptive window selection to balance variance reduction against structural breaks .

  # Conclusion

  In this paper, we evaluated the performance limits of moving average smoothing versus a naive last-value persistence forecast on short synthetic time series. Through rigorous Monte Carlo evaluation across 800 trials, we established that moving average smoothing achieves consistent error reductions (19.35\% overall, $p = 0.0226$; 31.08\% in pure white noise, $p < 1e-17$). Our sensitivity analysis across window sizes $K \in \{1, 2, 3, 4, 5, 10\}$ maps out the precise operational boundaries where classical smoothing outperforms persistence, establishing a rigorous performance baseline for modern time series forecasting research .

  # References

  [1] George E. P. Box and Gwilym M. Jenkins. *Time Series Analysis: Forecasting and Control*. Holden-Day, 1970.

  [2] Chris Chatfield. *The Analysis of Time Series: An Introduction*. Chapman and Hall/CRC, 6th edition, 2003.

  [3] Rob J. Hyndman and George Athanasopoulos. *Forecasting: Principles and Practice*. OTexts, 2nd edition, 2018.

  [4] A. Botchkarev. Performance Metrics (Error Measures) in Machine Learning Regression, Forecasting and Prognostics: Properties and Typology. *Interdisciplinary Journal of Information, Knowledge, and Management*, 13:189--213, 2018. doi: 10.28945/4184.
summary: >-
  An empirical audit comparing 3-point moving average and window sensitivity against naive persistence across synthetic time
  series datasets, demonstrating a statistically significant 19.35% MSE reduction.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
title: Forecasting Pipeline Overview
caption: >-
  End-to-end evaluation pipeline comparing naive last-value persistence against rolling moving average smoothing across varying
  window sizes $K$ and stochastic AR($1$) noise processes.
image_gen_detailed_description: >-
  Horizontal flow diagram, left to right. Three main blocks: 'Input Noisy Time Series ($X_t = \mu + \epsilon_t$)' (gray box),
  branching into 'Naive Persistence Baseline (\hat{X}_{T+1} = X_T)' (blue box) and 'Rolling Moving Average ($\hat{X}_{T+1}
  = \frac{1}{K}\sum X_{T-i}$)' (green box), feeding into 'Comparative Evaluation & MSE/MAE Scoring' (orange box). Sans-serif
  font, clean white background, professional academic style.
aspect_ratio: '21:9'
summary: >-
  End-to-end pipeline comparing naive persistence and rolling moving average smoothing.
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
title: MSE Scaling Across Noise Standard Deviations
caption: >-
  Comparison of empirical Mean Squared Error (MSE) between the naive persistence baseline and the 3-point moving average across
  noise standard deviations $\sigma \in \{0.5, 1.0, 2.0\}$. The 3-point moving average consistently achieves a 31.08% MSE
  reduction ($p < 1e-17$) across all noise magnitudes.
image_gen_detailed_description: >-
  Grouped bar chart. X-axis: noise standard deviation levels ($\sigma = 0.5$, $\sigma = 1.0$, $\sigma = 2.0$). Y-axis: Mean
  Squared Error (MSE, range 0 to 8). Two bars per group: Naive Persistence (dark blue, heights: 0.4856, 1.9426, 7.7702) and
  3-Point Moving Average (teal, heights: 0.3347, 1.3389, 5.3556). Error bars and exact percentage labels (31.08% reduction)
  annotated above each group. Clean white background, sans-serif font.
aspect_ratio: '21:9'
summary: Bar chart comparing MSE across noise standard deviations.
figure_path: figures/fig2_v0.jpg

--- Item 3 ---
id: fig3
title: Window Size Sensitivity Analysis
caption: >-
  Sensitivity of Mean Squared Error (MSE) across rolling window sizes $K \in \{1, 2, 3, 4, 5, 10\}$ on synthetic noisy time
  series. Moderate windows ($K=3, 4$) minimize prediction error by balancing noise variance reduction with minimal lag, whereas
  $K=1$ equals naive persistence and $K=10$ incurs oversmoothing penalties.
image_gen_detailed_description: >-
  Line plot with markers. X-axis: Window size $K$ taking values 1, 2, 3, 4, 5, 10. Y-axis: Mean Squared Error (MSE, range
  1.4 to 2.0). A U-shaped or convex curve showing MSE decreasing from $K=1$ (MSE 1.9094) to a minimum around $K=3$ to $K=4$
  (MSE ~1.539), and rising again at $K=10$. Dashed horizontal line representing Naive Persistence baseline (MSE 1.9094). Clean
  white background, sans-serif font, clear legend.
aspect_ratio: '21:9'
summary: Line plot showing MSE sensitivity across window sizes K.
figure_path: figures/fig3_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-07-30 14:35:30 UTC

```
Test whether a 3-point moving average beats a naive last-value forecast on a short synthetic series. Keep the investigation minimal.
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-07-30 14:35:32 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figure JPEGs, and bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.jpg}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS use `[!htbp]` float placement (NOT `[t]` or `[h]` alone)
- ALWAYS constrain with `width` and `keepaspectratio` to prevent page takeover
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/*.jpg` — all figure images (pre-generated, copied into workspace)
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-30 14:35:32 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
