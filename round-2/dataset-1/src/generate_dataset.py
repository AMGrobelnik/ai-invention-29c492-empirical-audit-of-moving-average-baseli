#!/usr/bin/env python3
"""Generate synthetic AR(1) and Noise Time Series Dataset and evaluate moving average vs naive forecast."""

from loguru import logger
from pathlib import Path
import json
import sys
import numpy as np

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    logger.info("Starting synthetic AR(1) time series dataset generation & evaluation")
    np.random.seed(42)
    
    # Parameters
    phi_values = [0.0, 0.2, 0.5, 0.8]
    n_samples_per_phi = 100
    sequence_length = 50
    noise_std = 1.0
    
    dataset_records = []
    
    for phi in phi_values:
        for i in range(n_samples_per_phi):
            # Generate AR(1) process: x_t = phi * x_{t-1} + e_t
            noise = np.random.normal(0, noise_std, sequence_length)
            x = np.zeros(sequence_length)
            for t in range(1, sequence_length):
                x[t] = phi * x[t-1] + noise[t]
                
            # Evaluation: 3-point moving average vs naive last-value forecast
            # Target is x[t] given history up to t-1
            ma_errors = []
            naive_errors = []
            
            for t in range(3, sequence_length):
                actual = x[t]
                # Naive: last value
                pred_naive = x[t-1]
                # 3-point moving average: mean of x[t-1], x[t-2], x[t-3]
                pred_ma = np.mean(x[t-3:t])
                
                ma_errors.append((pred_ma - actual) ** 2)
                naive_errors.append((pred_naive - actual) ** 2)
                
            mse_ma = float(np.mean(ma_errors))
            mse_naive = float(np.mean(naive_errors))
            
            record = {
                "phi": phi,
                "sample_idx": i,
                "sequence": x.tolist(),
                "metrics": {
                    "mse_moving_average": mse_ma,
                    "mse_naive": mse_naive,
                    "improvement_over_naive": mse_naive - mse_ma
                }
            }
            dataset_records.append(record)
            
    output_dir = Path("/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/temp/datasets")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    full_path = output_dir / "full_synthetic_ar1_dataset.json"
    full_path.write_text(json.dumps({"examples": dataset_records}, indent=2))
    logger.info(f"Saved full dataset with {len(dataset_records)} examples to {full_path}")
    
    # Mini variant (first 3 items)
    mini_path = output_dir / "mini_synthetic_ar1_dataset.json"
    mini_path.write_text(json.dumps({"examples": dataset_records[:3]}, indent=2))
    logger.info(f"Saved mini dataset to {mini_path}")

    # Preview variant
    preview_path = output_dir / "preview_synthetic_ar1_dataset.json"
    preview_path.write_text(json.dumps({"examples": dataset_records[:3]}, indent=2))
    logger.info(f"Saved preview dataset to {preview_path}")

if __name__ == "__main__":
    main()
