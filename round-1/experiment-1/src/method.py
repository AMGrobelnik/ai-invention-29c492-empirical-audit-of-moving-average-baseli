#!/usr/bin/env python3
"""Compare 3-point moving average and naive last-value forecasting on synthetic noisy time series across multiple trials, formatted for exp_gen_sol_out schema."""

import json
import sys
from pathlib import Path
import numpy as np
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
Path("logs").mkdir(exist_ok=True)
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def generate_noisy_series(length: int = 20, noise_std: float = 1.0, seed: int = 42) -> np.ndarray:
    np.random.seed(seed)
    true_mean = 10.0
    series = true_mean + np.random.normal(0, noise_std, size=length)
    return series

@logger.catch(reraise=True)
def run_evaluation(num_trials: int = 100, length: int = 20, noise_std: float = 1.0) -> dict:
    logger.info(f"Starting evaluation with {num_trials} trials, length={length}, noise_std={noise_std}")
    
    examples = []
    ma_errors = []
    naive_errors = []
    
    for i in range(num_trials):
        seed_val = 1000 + i
        series = generate_noisy_series(length=length, noise_std=noise_std, seed=seed_val)
        true_next = 10.0 + np.random.normal(0, noise_std, size=None)
        
        ma_pred = float(np.mean(series[-3:]))
        naive_pred = float(series[-1])
        
        ma_err = (ma_pred - true_next) ** 2
        naive_err = (naive_pred - true_next) ** 2
        
        ma_errors.append(ma_err)
        naive_errors.append(naive_err)
        
        example = {
            "input": f"Synthetic time series of length {length} with noise std {noise_std}, seed {seed_val}",
            "output": f"True next value: {true_next:.4f}",
            "metadata_fold": i % 5,
            "predict_moving_average": f"{ma_pred:.4f}",
            "predict_naive": f"{naive_pred:.4f}",
            "metadata_mse_ma": float(ma_err),
            "metadata_mse_naive": float(naive_err)
        }
        examples.append(example)
        
    mse_ma = float(np.mean(ma_errors))
    mse_naive = float(np.mean(naive_errors))
    
    logger.info(f"Results -> MSE Moving Average: {mse_ma:.4f}, MSE Naive: {mse_naive:.4f}")
    
    dataset_obj = {
        "dataset": "synthetic_noisy_time_series",
        "examples": examples,
        "summary_metrics": {
            "mse_moving_average": mse_ma,
            "mse_naive": mse_naive,
            "num_trials": num_trials,
            "noise_std": noise_std,
            "length": length,
            "improvement_pct": float((mse_naive - mse_ma) / mse_naive * 100.0)
        }
    }
    return dataset_obj

@logger.catch(reraise=True)
def main():
    dataset_obj = run_evaluation(num_trials=100, length=20, noise_std=1.0)
    
    full_output = {
        "datasets": [dataset_obj]
    }
    
    workspace = Path("/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_experiment_1")
    
    (workspace / "method_out.json").write_text(json.dumps(full_output, indent=2))
    (workspace / "full_method_out.json").write_text(json.dumps(full_output, indent=2))
    
    mini_dataset = dict(dataset_obj)
    mini_dataset["examples"] = dataset_obj["examples"][:10]
    mini_output = {"datasets": [mini_dataset]}
    (workspace / "mini_method_out.json").write_text(json.dumps(mini_output, indent=2))
    
    preview_dataset = dict(dataset_obj)
    preview_dataset["examples"] = dataset_obj["examples"][:3]
    preview_output = {"datasets": [preview_dataset]}
    (workspace / "preview_method_out.json").write_text(json.dumps(preview_output, indent=2))
    
    logger.info("Successfully generated all schema-compliant JSON files.")

if __name__ == "__main__":
    main()
