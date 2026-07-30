import json
import numpy as np
import os

def evaluate_forecasting(data_path, output_path):
    print(f"Loading data from {data_path}...")
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    examples = data['datasets'][0]['examples']
    print(f"Total trials loaded: {len(examples)}")
    
    k_values = [1, 2, 3, 4, 5, 10]
    new_examples = []
    
    for i, ex in enumerate(examples):
        series = np.array(json.loads(ex['input']))
        true_mean = float(ex['output'])
        length = ex['metadata_length']
        noise_var = ex['metadata_noise_variance']
        trial_id = ex['metadata_trial_id']
        
        if len(series) > 1:
            actuals = series[1:]
            naive_preds = series[:-1]
            naive_mse = float(np.mean((actuals - naive_preds) ** 2))
        else:
            naive_mse = 0.0
            
        ex_out = {
            "input": ex['input'],
            "output": ex['output'],
            "metadata_trial_id": trial_id,
            "metadata_length": length,
            "metadata_noise_variance": noise_var,
            "predict_naive": str(naive_mse)
        }
        
        for k in k_values:
            if len(series) >= k + 1:
                actuals = series[k:]
                preds = []
                for t in range(k, len(series)):
                    window = series[t-k:t]
                    preds.append(np.mean(window))
                preds = np.array(preds)
                ma_mse = float(np.mean((actuals - preds) ** 2))
            else:
                ma_mse = naive_mse
            ex_out[f"predict_MA_K_{k}"] = str(ma_mse)
            
        new_examples.append(ex_out)
        
    final_output = {
        "datasets": [
            {
                "dataset": data['datasets'][0]['dataset'],
                "examples": new_examples
            }
        ]
    }
    
    print("Saving results to", output_path)
    with open(output_path, 'w') as f:
        json.dump(final_output, f, indent=2)
    print("Evaluation completed successfully.")

if __name__ == '__main__':
    import sys
    data_file = "full_data_out.json" if len(sys.argv) > 1 and sys.argv[1] == "full" else "mini_data_out.json"
    output_path = "method_out.json"
    evaluate_forecasting(data_file, output_path)
