import json

# Copy full_eval_out.json to eval_out.json as expected by TODO 1
with open("/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/results/full_eval_out.json", "r") as f:
    data = json.load(f)

with open("/ai-inventor/aii_data/runs/run_b5__bxLYNiMo/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/eval_out.json", "w") as f:
    json.dump(data, f, indent=2)

print("Copied full_eval_out.json to eval_out.json successfully.")
