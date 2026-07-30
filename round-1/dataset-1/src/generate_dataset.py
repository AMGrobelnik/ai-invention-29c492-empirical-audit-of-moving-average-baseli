import json
import os
import numpy as np

def generate_synthetic_data():
    np.random.seed(42)
    lengths = [10, 20, 50, 100]
    variances = [0.1, 0.5, 1.0, 2.0]
    num_trials_per_setting = 50
    
    dataset = []
    trial_id = 0
    
    for T in lengths:
        for var in variances:
            sigma = np.sqrt(var)
            for trial in range(num_trials_per_setting):
                true_mean = 10.0
                noise = np.random.normal(0, sigma, size=T)
                series = true_mean + noise
                
                entry = {
                    "trial_id": trial_id,
                    "length": T,
                    "noise_variance": var,
                    "true_mean": true_mean,
                    "series": series.tolist()
                }
                dataset.append(entry)
                trial_id += 1
                
    os.makedirs("/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/temp/datasets", exist_ok=True)
    out_path = "/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/temp/datasets/data_out.json"
    with open(out_path, "w") as f:
        json.dump(dataset, f, indent=2)
    print(f"Successfully generated {len(dataset)} trials and saved to {out_path}")

if __name__ == "__main__":
    generate_synthetic_data()
