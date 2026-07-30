#!/usr/bin/env python3
import json
from pathlib import Path

def main():
    workspace = Path("/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_experiment_1")
    data = json.loads((workspace / "method_out.json").read_text())
    
    # 1. Full
    (workspace / "full_method_out.json").write_text(json.dumps(data, indent=2))
    
    # 2. Mini
    mini_data = {
        "mse_moving_average": data.get("mse_moving_average"),
        "mse_naive": data.get("mse_naive"),
        "improvement_pct": data.get("improvement_pct")
    }
    (workspace / "mini_method_out.json").write_text(json.dumps(mini_data, indent=2))
    
    # 3. Preview
    preview_data = {
        "mse_moving_average": data.get("mse_moving_average"),
        "mse_naive": data.get("mse_naive"),
        "num_trials": data.get("num_trials")
    }
    (workspace / "preview_method_out.json").write_text(json.dumps(preview_data, indent=2))
    print("Successfully generated full, mini, and preview JSON files.")

if __name__ == "__main__":
    main()
