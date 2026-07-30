# /// script
# dependencies = ["numpy", "pydantic"]
# ///

import json
import os

def process_data():
    src_path = "/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/temp/datasets/data_out.json"
    with open(src_path, "r") as f:
        trials = json.load(f)
        
    examples = []
    for trial in trials:
        examples.append({
            "input": json.dumps(trial["series"]),
            "output": str(trial["true_mean"]),
            "metadata_trial_id": trial["trial_id"],
            "metadata_length": trial["length"],
            "metadata_noise_variance": trial["noise_variance"]
        })
        
    dataset_group = {
        "datasets": [
            {
                "dataset": "synthetic_noisy_time_series",
                "examples": examples
            }
        ]
    }
    
    out_path = "/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json"
    with open(out_path, "w") as f:
        json.dump(dataset_group, f, indent=2)
        
    # Mini version (first 3 examples)
    mini_data = {
        "datasets": [
            {
                "dataset": "synthetic_noisy_time_series",
                "examples": examples[:3]
            }
        ]
    }
    with open("/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/mini_data_out.json", "w") as f:
        json.dump(mini_data, f, indent=2)
        
    # Preview version (first 10 examples)
    preview_data = {
        "datasets": [
            {
                "dataset": "synthetic_noisy_time_series",
                "examples": examples[:10]
            }
        ]
    }
    with open("/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/preview_data_out.json", "w") as f:
        json.dump(preview_data, f, indent=2)
        
    print(f"Standardized {len(examples)} examples into full, mini, and preview files.")

if __name__ == "__main__":
    process_data()
