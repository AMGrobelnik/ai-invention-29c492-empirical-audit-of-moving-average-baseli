#!/usr/bin/env python3
"""Evaluation script comparing 3-point moving average vs naive forecast across noise levels."""

import json
import sys
from pathlib import Path
import numpy as np
from scipy import stats
from loguru import logger
import matplotlib.pyplot as plt

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
Path("logs").mkdir(exist_ok=True)
logger.add("logs/eval.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    logger.info("Starting comprehensive evaluation of moving average vs naive forecast")
    
    # Load method output
    method_out_path = Path("/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method_out.json")
    if not method_out_path.exists():
        logger.error(f"method_out.json not found at {method_out_path}")
        sys.exit(1)
        
    data = json.loads(method_out_path.read_text())
    multi_noise = data.get("multi_noise_analysis", {})
    
    # Re-run a trial loop with paired samples to compute paired t-test p-values across trials per noise level
    evaluation_results = {}
    
    for key, info in multi_noise.items():
        noise_std = info["noise_std"]
        num_trials = info["num_trials"]
        length = info["length"]
        
        logger.info(f"Evaluating noise_std={noise_std} with {num_trials} trials for statistical significance...")
        
        ma_errors_sq = []
        naive_errors_sq = []
        
        for i in range(num_trials):
            np.random.seed(1000 + i)
            true_mean = 10.0
            series = true_mean + np.random.normal(0, noise_std, size=length)
            true_next = 10.0 + np.random.normal(0, noise_std)
            
            ma_pred = float(np.mean(series[-3:]))
            naive_pred = float(series[-1])
            
            ma_errors_sq.append((ma_pred - true_next) ** 2)
            naive_errors_sq.append((naive_pred - true_next) ** 2)
            
        ma_arr = np.array(ma_errors_sq)
        naive_arr = np.array(naive_errors_sq)
        
        # Paired t-test on squared errors (or absolute errors)
        t_stat, p_value = stats.ttest_rel(naive_arr, ma_arr) # naive - ma > 0 implies naive error > ma error
        
        mse_ma = float(np.mean(ma_arr))
        mse_naive = float(np.mean(naive_arr))
        improvement_pct = float((mse_naive - mse_ma) / mse_naive * 100.0)
        
        evaluation_results[key] = {
            "noise_std": noise_std,
            "mse_moving_average": mse_ma,
            "mse_naive": mse_naive,
            "improvement_pct": improvement_pct,
            "paired_t_statistic": float(t_stat),
            "paired_p_value": float(p_value),
            "statistically_significant_05": bool(p_value < 0.05)
        }
        logger.info(f"[{key}] MSE MA: {mse_ma:.4f}, MSE Naive: {mse_naive:.4f}, Improvement: {improvement_pct:.2f}%, p-value: {p_value:.2e}")

    # Create visualization
    noise_stds = [res["noise_std"] for res in evaluation_results.values()]
    mse_mas = [res["mse_moving_average"] for res in evaluation_results.values()]
    mse_naives = [res["mse_naive"] for res in evaluation_results.values()]
    
    plt.figure(figsize=(8, 5))
    plt.plot(noise_stds, mse_mas, marker='o', label='3-Point Moving Average', linewidth=2)
    plt.plot(noise_stds, mse_naives, marker='s', label='Naive Last-Value Forecast', linewidth=2, linestyle='--')
    plt.xlabel('Noise Standard Deviation ($\sigma$)', fontsize=12)
    plt.ylabel('Mean Squared Error (MSE)', fontsize=12)
    plt.title('Forecast MSE Comparison Across Noise Levels', fontsize=14)
    plt.legend(fontsize=11)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    
    fig_path = Path("/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1/forecast_comparison.png")
    plt.savefig(fig_path, dpi=300)
    plt.close()
    logger.info(f"Saved visualization to {fig_path}")

    # Final summary output matching schema expectations
    final_output = {
        "evaluation_summary": {
            "primary_mse_moving_average": data["mse_moving_average"],
            "primary_mse_naive": data["mse_naive"],
            "primary_improvement_pct": data["improvement_pct"],
            "num_trials": data["num_trials"]
        },
        "detailed_results": evaluation_results,
        "figure_path": str(fig_path)
    }
    
    out_json_path = Path("/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1/eval_out.json")
    out_json_path.write_text(json.dumps(final_output, indent=2))
    logger.info(f"Saved evaluation output to {out_json_path}")

if __name__ == "__main__":
    main()
