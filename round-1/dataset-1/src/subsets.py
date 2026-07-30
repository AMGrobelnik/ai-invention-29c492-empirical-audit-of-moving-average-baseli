# /// script
# dependencies = ["pydantic"]
# ///

import json

def generate_subsets():
    path = "/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json"
    with open(path, "r") as f:
        data = json.load(f)
        
    # Mini version (first 5 examples per dataset)
    mini_data = {"datasets": []}
    for ds in data["datasets"]:
        mini_ds = {
            "dataset": ds["dataset"],
            "examples": ds["examples"][:5]
        }
        mini_data["datasets"].append(mini_ds)
        
    with open("/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/mini_data_out.json", "w") as f:
        json.dump(mini_data, f, indent=2)
        
    with open("/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/preview_data_out.json", "w") as f:
        json.dump(mini_data, f, indent=2)
        
    print("Generated mini and preview datasets successfully.")

if __name__ == "__main__":
    generate_subsets()
