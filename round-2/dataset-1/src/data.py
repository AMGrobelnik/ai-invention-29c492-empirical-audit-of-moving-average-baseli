#!/usr/bin/env python3
"""Standardize synthetic AR(1) dataset to exp_sel_data_out.json schema."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    logger.info("Starting data standardization for synthetic AR(1) dataset")
    
    input_path = Path("/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/temp/datasets/full_synthetic_ar1_dataset.json")
    raw_data = json.loads(input_path.read_text())
    
    examples = []
    for item in raw_data["examples"]:
        # Each example: input is sequence up to t-1, output is next value or metrics
        seq = item["sequence"]
        # Let's define input as the sequence string representation, output as the last value
        input_str = json.dumps(seq[:-1])
        output_str = str(seq[-1])
        
        example = {
            "input": input_str,
            "output": output_str,
            "metadata_phi": item["phi"],
            "metadata_sample_idx": item["sample_idx"],
            "metadata_mse_moving_average": item["metrics"]["mse_moving_average"],
            "metadata_mse_naive": item["metrics"]["mse_naive"],
            "metadata_improvement_over_naive": item["metrics"]["improvement_over_naive"],
            "metadata_task_type": "time_series_forecasting"
        }
        examples.append(example)
        
    dataset_group = {
        "dataset": "synthetic_ar1_time_series",
        "examples": examples
    }
    
    output_data = {
        "datasets": [dataset_group]
    }
    
    output_path = Path("/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/full_data_out.json")
    output_path.write_text(json.dumps(output_data, indent=2))
    logger.info(f"Saved standardized dataset with {len(examples)} examples to {output_path}")

if __name__ == "__main__":
    main()
