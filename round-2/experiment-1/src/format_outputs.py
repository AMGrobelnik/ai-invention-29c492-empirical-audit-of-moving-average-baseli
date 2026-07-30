import json

def format_output():
    with open('method_out.json', 'r') as f:
        data = json.load(f)
    
    with open('full_method_out.json', 'w') as f:
        json.dump(data, f, indent=2)
        
    mini_data = {
        "datasets": [
            {
                "dataset": data["datasets"][0]["dataset"],
                "examples": data["datasets"][0]["examples"][:3]
            }
        ]
    }
    with open('mini_method_out.json', 'w') as f:
        json.dump(mini_data, f, indent=2)
        
    preview_data = {
        "datasets": [
            {
                "dataset": data["datasets"][0]["dataset"],
                "examples": data["datasets"][0]["examples"][:1]
            }
        ]
    }
    with open('preview_method_out.json', 'w') as f:
        json.dump(preview_data, f, indent=2)

    print("Generated successfully.")

if __name__ == '__main__':
    format_output()
