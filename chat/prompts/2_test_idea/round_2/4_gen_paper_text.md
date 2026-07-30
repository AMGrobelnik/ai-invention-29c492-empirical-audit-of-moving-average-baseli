# gen_paper_text — test_idea

> Phase: `invention_loop` · round 2 · `gen_paper_text`
> Run: `run_b5__bxLYNiMo` — Empirical Audit of Moving Average Baselines in Short-Horizon Time Series Forecasting
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-30 14:22:11 UTC

````
<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

# Introduction

Short-horizon time series forecasting is a ubiquitous challenge across financial markets, sensor networks, supply chain management, and operational monitoring. In many practical deployment scenarios, time series data are observed over limited temporal windows and contaminated by substantial high-frequency observational noise. A central question confronting practitioners is how to formulate robust baseline forecasts when sample sizes are small and signal-to-noise ratios are low.

Among classical univariate forecasting techniques, the naive last-value forecast (or persistence model) serves as the canonical baseline. By assuming that the future value equals the most recent observation, the naive model requires no parameter estimation and introduces zero phase lag. However, in the presence of additive white noise, persistence forecasting directly extrapolates the most recent noise realization rather than the underlying mean process, leading to severe error amplification. To mitigate high-frequency volatility, classical smoothing methods such as moving averages aggregate successive observations to estimate the local level.

Despite the ubiquity of moving averages in technical analysis and statistical control [1], rigorous quantitative comparisons against naive persistence under controlled synthetic noise regimes are frequently overlooked in modern machine learning benchmarks, which often jump directly to complex recurrent neural networks or transformer architectures. Understanding the exact performance boundaries between simple smoothing and persistence is essential for establishing rigorous performance floors.

In this work, we investigate the hypothesis that a 3-point moving average outperforms the naive last-value forecast on short synthetic time series exhibiting stationary means and additive Gaussian noise. Utilizing 1,000 independent Monte Carlo trials across multiple noise variance levels (sigma in {0.5, 1.0, 2.0}), we evaluate both forecasting strategies under identical conditions [ARTIFACT:art_TEePI__hgyqJ]. Our results conclusively demonstrate that the 3-point moving average achieves a mean squared error (MSE) reduction of 31.08% relative to the naive baseline, supported by robust paired t-tests (t = 8.83, p < 1e-17) [ARTIFACT:art_Qq6PIWob3zAd].

[FIGURE:fig1]

Our key contributions are summarized as follows:
- We formulate a controlled empirical evaluation framework comparing 3-point moving average smoothing against naive persistence across 800 synthetic time series trials [ARTIFACT:art_j0ycG0HOL2aX].
- We demonstrate a consistent 31.08% MSE reduction achieved by the 3-point moving average across noise standard deviations of 0.5, 1.0, and 2.0 [ARTIFACT:art_Qq6PIWob3zAd].
- We analyze the theoretical trade-offs between variance reduction and lag introduction in short-horizon univariate forecasting.

# Related Work

Univariate time series forecasting has a rich history rooted in classical statistical literature. The foundational frameworks established by Box and Jenkins [2] formalized autoregressive integrated moving average (ARIMA) models, demonstrating how moving average components capture short-term dependencies and smooth stochastic perturbations. Similarly, exponential smoothing and simple moving averages have long served as bedrock techniques in industrial inventory control and economic forecasting [3].

In modern forecasting literature, empirical evaluations regularly benchmark sophisticated machine learning models against classical statistical baselines. Large-scale forecasting competitions such as the M-competitions (e.g., M4 and M5) have repeatedly highlighted that well-tuned classical statistical methods and simple combination baselines frequently match or exceed complex deep learning architectures on noisy, irregular time series [4]. Botchkarev [4] provides a comprehensive taxonomy of regression and forecasting error measures, emphasizing the critical importance of utilizing Mean Squared Error (MSE) and Mean Absolute Error (MAE) under appropriate distributional assumptions.

Despite the prevalence of advanced neural architectures, understanding the fundamental mechanics of baseline smoothing versus persistence in micro-scale horizons remains vital. Our work bridges this gap by isolating the performance of a minimal 3-point moving average against the naive persistence baseline under rigorous synthetic noise conditions.

# Methodology

We consider a univariate stationary time series process where each observed value X_t consists of an underlying stationary mean mu perturbed by additive Gaussian white noise:

X_t = mu + epsilon_t, where epsilon_t ~ N(0, sigma^2)

Given a discrete sequence of observations up to time T, our objective is to forecast the future value X_{T+1}. We evaluate two competing forecasting strategies:

## Naive Last-Value Forecast
The naive forecasting model assumes persistence of the most recent observation:

hat{X}_{T+1}^{naive} = X_T = mu + epsilon_T

The expected squared error for the naive forecast is:

E[ (X_{T+1} - hat{X}_{T+1}^{naive})^2 ] = E[ (epsilon_{T+1} - epsilon_T)^2 ] = 2 * sigma^2

## 3-Point Moving Average Forecast
The 3-point moving average (MA) computes the arithmetic mean of the three most recent observations to estimate the local level:

hat{X}_{T+1}^{MA} = (1/3) * sum_{i=0}^{2} X_{T-i} = mu + (1/3) * sum_{i=0}^{2} epsilon_{T-i}

Assuming independence of noise terms across time steps, the expected squared error for the 3-point moving average is:

E[ (X_{T+1} - hat{X}_{T+1}^{MA})^2 ] = E[ (epsilon_{T+1} - (1/3)*(epsilon_T + epsilon_{T-1} + epsilon_{T-2}))^2 ] = (1 + 1/9 + 1/9 + 1/9) * sigma^2 = (4/3) * sigma^2 approx 1.333 * sigma^2

Comparing the theoretical mean squared errors, the ratio of the moving average MSE to the naive MSE is (4/3) / 2 = 2/3 approx 0.667, implying a theoretical error reduction of approximately 33.3% in asymptotic stationary regimes.

[FIGURE:fig2]

# Experiments and Results

To empirically validate our theoretical derivation, we construct a synthetic dataset comprising 800 time series trials [ARTIFACT:art_j0ycG0HOL2aX] evaluated across 1,000 independent Monte Carlo iterations per condition [ARTIFACT:art_TEePI__hgyqJ]. We test sequence lengths T in {10, 20, 50, 100} and noise standard deviation levels sigma in {0.5, 1.0, 2.0}.

Table 1 summarizes the empirical Mean Squared Error (MSE) results for both forecasting methods across all evaluated noise standard deviation levels.

| Noise Level (sigma) | Naive MSE | Moving Average (3-Pt) MSE | MSE Reduction (%) | p-value |
| :--- | :--- | :--- | :--- | :--- |
| sigma = 0.5 | 0.4856 | 0.3347 | 31.08% | < 1e-17 |
| sigma = 1.0 | 1.9426 | 1.3389 | 31.08% | < 1e-17 |
| sigma = 2.0 | 7.7702 | 5.3556 | 31.08% | < 1e-17 |
| **Aggregated** | **1.9426** | **1.3389** | **31.08%** | **< 1e-17** |

[FIGURE:fig3]

As detailed in Table 1, the 3-point moving average consistently outperforms the naive last-value forecast across all noise conditions, achieving an aggregate MSE of 1.3389 compared to 1.9426 for the naive baseline. This represents an empirical error reduction of 31.08%, perfectly aligning with our theoretical expectation of variance attenuation in additive Gaussian noise regimes [ARTIFACT:art_Qq6PIWob3zAd].

# Discussion

Our empirical findings demonstrate that simple temporal smoothing robustly outperforms persistence in stationary noisy time series. While the naive model avoids introducing lag, its susceptibility to instantaneous noise realization dominates the error profile. By averaging over three time steps, the moving average dampens the noise variance by a factor of 4/3 relative to 2 for persistence.

However, these findings must be contextualized within certain methodological limitations:
1. **Stationarity Assumption**: The synthetic generation assumes a constant underlying mean mu. In non-stationary regimes characterized by strong trends or structural breaks, a 3-point moving average would introduce undesirable lag, whereas naive persistence or adaptive exponential smoothing might perform better.
2. **Fixed Window Hyperparameter**: We evaluated a fixed 3-point window. While optimal for suppressing moderate high-frequency noise without excessive lag, longer windows (e.g., K > 5) risk oversmoothing genuine short-term signal fluctuations in dynamic environments.

# Conclusion

In this paper, we evaluated the performance limits of a 3-point moving average versus a naive last-value persistence forecast on short synthetic time series with high-frequency noise. Through rigorous Monte Carlo evaluation across 1,000 trials, we established that the 3-point moving average achieves a consistent 31.08% reduction in mean squared error (p < 1e-17). These results underscore the enduring utility of classical smoothing baselines and provide a principled foundation for short-horizon forecasting research.

# References

[1] Chris Chatfield. *The Analysis of Time Series: An Introduction*. Chapman and Hall/CRC, 6th edition, 2003.

[2] George E. P. Box and Gwilym M. Jenkins. *Time Series Analysis: Forecasting and Control*. Holden-Day, 1970.

[3] Rob J. Hyndman and George Ahanasopoulos. *Forecasting: Principles and Practice*. OTexts, 2nd edition, 2018.

[4] A. Botchkarev. Performance Metrics (Error Measures) in Machine Learning Regression, Forecasting and Prognostics: Properties and Typology. *Interdisciplinary Journal of Information, Knowledge, and Management*, 2018. doi: 10.28945/4184.

</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

- [MAJOR] (novelty) The theoretical equivalence and variance reduction ratios for moving averages over iid noise are standard textbook results in time series analysis (e.g., Box & Jenkins, Chatfield), which limits the novelty of the core analytical contribution.
  Action: Refosition the contribution clearly as an empirical baseline audit and performance floor study for modern machine learning benchmarks that overlook classical smoothing.
- [MAJOR] (scope) The evaluation is restricted solely to stationary white noise around a constant mean. Real-world short-horizon time series frequently exhibit serial correlation (AR/MA structures) or slight non-stationarity.
  Action: Include an extension evaluating performance on AR(1) processes with varying autoregressive coefficients phi to determine the break-even point where lag penalties outweigh variance reduction.
- [MINOR] (rigor) The choice of K=3 is fixed without justifying why K=3 was selected over K=2 or K=5 in the main text other than general reference to short horizons.
  Action: Add a sensitivity analysis table or plot showing MSE performance across window sizes K in {1, 2, 3, 4, 5, 10}.
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

kind: hypothesis
title: Moving Average vs Naive Forecast Baseline Audit
hypothesis: >-
  A 3-point moving average outperforms a naive last-value forecast on short stationary time series with high-frequency noise,
  achieving robust error reduction across additive white noise and mild AR(1) processes, with performance bounded by lag penalties
  as window size and persistence increase.
motivation: >-
  Understanding the limits of smoothing vs persistence in noisy short-horizon forecasting.
assumptions:
- The time series has stationary mean with additive noise.
- The noise variance is sufficiently high to warrant smoothing.
- Sample size is small.
investigation_approach: >-
  Generate synthetic noisy time series and compare Mean Squared Error (MSE) of 3-point moving average against naive last-value
  forecast.
success_criteria: Lower MSE for the 3-point moving average across multiple synthetic trials.
related_works:
- >-
  Classical time series forecasting benchmarks (Box-Jenkins style persistence and smoothing comparisons).
inspiration: Classical statistical forecasting and baseline comparisons.
terms:
- term: Moving Average
  definition: >-
    A calculation used to analyze data points by creating a series of averages of different subsets of the full data set.
- term: Naive Forecast
  definition: >-
    A forecasting method that assumes the next period's value will be equal to the current period's value.
summary: >-
  Comparing a 3-point moving average to a naive last-value forecast on synthetic noisy data.
_relation_rationale: >-
  Refines hypothesis to include AR(1) serial correlation and window sensitivity based on reviewer feedback.
_confidence_delta: increased
_key_changes:
- >-
  Extended scope to evaluate performance on AR(1) processes with varying autoregressive coefficients.
- Added sensitivity analysis across window sizes K in {1, 2, 3, 4, 5, 10}.
- >-
  Positioned the study explicitly as an empirical baseline audit and performance floor for time series modeling.
relation_type: evolution
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 6 research artifacts across all iterations.

--- Item 1 ---
id: art_j0ycG0HOL2aX
type: dataset
title: Synthetic Noisy Time Series Dataset
summary: >-
  This comprehensive dataset artifact provides 800 synthetic stationary time series trials generated with varying sequence
  lengths (T=10, 20, 50, 100) and additive Gaussian noise variance levels (sigma^2 = 0.1, 0.5, 1.0, 2.0). Each trial includes
  the raw time series array, ground truth mean, noise variance, trial ID, and length. Structured in standardized JSON format
  with full, mini, and preview variants to rigorously evaluate moving average forecasting performance relative to naive last-value
  forecasting across diverse noise conditions and sample sizes.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 2 ---
id: art_TEePI__hgyqJ
type: experiment
title: Moving Average vs Naive Forecast
summary: >-
  This experiment provides a rigorous empirical evaluation comparing a 3-point moving average smoothing technique against
  a naive last-value persistence forecasting baseline on synthetic noisy time series data across 1,000 independent trials.
  In time series analysis and forecasting tasks, distinguishing between genuine underlying signal dynamics and high-frequency
  observational noise is critical for predictive accuracy. The naive baseline forecasts the future value by simply persisting
  the most recent observed value, making it highly susceptible to random noise fluctuations. Conversely, the 3-point moving
  average aggregates the last three observations to smooth out additive Gaussian noise, providing a more robust estimate of
  the local level. Our comprehensive evaluation across multiple noise levels (standard deviations of 0.5, 1.0, and 2.0) demonstrates
  that the 3-point moving average consistently outperforms the naive baseline, achieving a mean squared error (MSE) reduction
  of approximately 31.08% across all tested noise configurations. These findings validate that simple window-based smoothing
  is superior to persistence forecasting in stationary noisy regimes, offering a dependable baseline for subsequent time series
  modeling research.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 3 ---
id: art_Qq6PIWob3zAd
type: evaluation
title: Moving Average vs Naive Forecast Evaluation
summary: >-
  This evaluation artifact provides a rigorous quantitative comparison between a 3-point moving average forecasting method
  and a naive last-value baseline across multiple synthetic noisy time series generation settings. Utilizing 1,000 independent
  Monte Carlo trials for each evaluated noise standard deviation level (0.5, 1.0, and 2.0), we compute empirical Mean Squared
  Error (MSE) metrics, percentage error reduction improvements, and conduct rigorous paired t-tests to establish statistical
  significance. The results conclusively demonstrate that the 3-point moving average achieves a consistent and statistically
  significant error reduction of approximately 31.08% compared to the naive last-value forecast (with paired t-statistics
  around 8.83 and p-values well below 1e-17). Furthermore, we generate publication-ready visualization figures illustrating
  the error scaling across noise levels, structured schema-compliant JSON outputs (full, mini, and preview variants adhering
  to exp_eval_sol_out), and fully reproducible dependency specifications via pyproject.toml.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

--- Item 4 ---
id: art_UGSk_PRiSYxa
type: dataset
title: Synthetic AR(1) and Noise Time Series Dataset
summary: >-
  This artifact provides a comprehensive synthetic time series dataset specifically designed to evaluate and benchmark time
  series forecasting methods across diverse stochastic regimes. It incorporates rigorous AR(1) autoregressive processes with
  varying coefficients phi in {0.0, 0.2, 0.5, 0.8}, configurable noise levels, and precise sequence lengths. Furthermore,
  the dataset evaluates 3-point moving average forecasting performance against a naive last-value baseline across numerous
  simulated trials, capturing nuanced error metrics and performance improvements. All generated trials are meticulously formatted,
  validated, and structured into full, mini, and preview JSON variants adhering strictly to standard experimental dataset
  schemas, ensuring robust reproducibility and seamless integration into downstream machine learning pipelines and research
  evaluations.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 5 ---
id: art_od0orPfZGnpY
type: experiment
title: Moving Average vs Naive Baseline Audit
summary: >-
  This experiment evaluates rolling moving average forecasting across window sizes K in {1, 2, 3, 4, 5, 10} and naive last-value
  persistence on 800 synthetic stationary time series trials with varying sequence lengths and noise variances. The study
  investigates the impact of smoothing window parameters on forecasting accuracy, measuring both Mean Squared Error (MSE)
  and Mean Absolute Error (MAE) across diverse noise conditions. By comparing moving average models side-by-side with the
  naive persistence baseline within a unified experimental pipeline, we provide rigorous empirical evidence regarding noise
  reduction and error propagation in short-horizon time series forecasting. The findings demonstrate systematic performance
  variations across different window lengths, highlighting optimal parameter regimes for stationary noisy data.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 6 ---
id: art_SPzlyDfFdNjq
type: evaluation
title: Moving Average vs Naive Forecast Evaluation
summary: >-
  This evaluation artifact provides a rigorous statistical analysis of the moving average baseline versus the naive persistence
  baseline across 100 independent synthetic time series trials. We evaluate predictive accuracy using Mean Squared Error (MSE),
  paired t-tests (yielding t = 2.316, p = 0.0226), and relative error reduction (19.35%). Furthermore, we conduct an extensive
  sensitivity analysis varying window sizes K and AR(1) autoregressive coefficients phi to map out robustness limits and break-even
  regimes.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 3 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

title: Synthetic AR(1) and Noise Time Series Dataset
summary: >-
  This artifact provides a comprehensive synthetic time series dataset specifically designed to evaluate and benchmark time
  series forecasting methods across diverse stochastic regimes. It incorporates rigorous AR(1) autoregressive processes with
  varying coefficients phi in {0.0, 0.2, 0.5, 0.8}, configurable noise levels, and precise sequence lengths. Furthermore,
  the dataset evaluates 3-point moving average forecasting performance against a naive last-value baseline across numerous
  simulated trials, capturing nuanced error metrics and performance improvements. All generated trials are meticulously formatted,
  validated, and structured into full, mini, and preview JSON variants adhering strictly to standard experimental dataset
  schemas, ensuring robust reproducibility and seamless integration into downstream machine learning pipelines and research
  evaluations.
id: art_UGSk_PRiSYxa
type: dataset

title: Moving Average vs Naive Baseline Audit
summary: >-
  This experiment evaluates rolling moving average forecasting across window sizes K in {1, 2, 3, 4, 5, 10} and naive last-value
  persistence on 800 synthetic stationary time series trials with varying sequence lengths and noise variances. The study
  investigates the impact of smoothing window parameters on forecasting accuracy, measuring both Mean Squared Error (MSE)
  and Mean Absolute Error (MAE) across diverse noise conditions. By comparing moving average models side-by-side with the
  naive persistence baseline within a unified experimental pipeline, we provide rigorous empirical evidence regarding noise
  reduction and error propagation in short-horizon time series forecasting. The findings demonstrate systematic performance
  variations across different window lengths, highlighting optimal parameter regimes for stationary noisy data.
id: art_od0orPfZGnpY
type: experiment

title: Moving Average vs Naive Forecast Evaluation
summary: >-
  This evaluation artifact provides a rigorous statistical analysis of the moving average baseline versus the naive persistence
  baseline across 100 independent synthetic time series trials. We evaluate predictive accuracy using Mean Squared Error (MSE),
  paired t-tests (yielding t = 2.316, p = 0.0226), and relative error reduction (19.35%). Furthermore, we conduct an extensive
  sensitivity analysis varying window sizes K and AR(1) autoregressive coefficients phi to map out robustness limits and break-even
  regimes.
id: art_SPzlyDfFdNjq
type: evaluation
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison):
  {"id": "fig3", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: latency (seconds, 0-5). Values: PostgreSQL=4.6s (red), Bao=2.8s (blue), RLQOpt=2.0s (green). Error bars +/-0.3-0.8. Sans-serif font, white background.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero):
  {"id": "fig1", "title": "System Architecture", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "Detailed image generation prompt \u2014 axes, labels, ALL numeric values, colors, aspect ratio, layout. The image generator cannot read files; this is its ONLY input.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-07-30 14:22:11 UTC

```
Test whether a 3-point moving average beats a naive last-value forecast on a short synthetic series. Keep the investigation minimal.
```

### [3] SKILL-INPUT — aii-paper-writing · 2026-07-30 14:22:11 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: Academic paper writing guidance for AI research. Covers paper structure, figure placeholders, bibliography building with Semantic Scholar, and citation rules. Does NOT cover LaTeX compilation or figure file generation — see aii-paper-to-latex for that.
---

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-30 14:22:13 UTC

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
