'''
The Task: Create a function get_nested_value(data_dict, key_path).

The Input: A deeply nested dictionary and a string path (e.g., "aws.region.primary").

The Goal: Return the value at that path. If the path doesn't exist, return a default value of None.

Example: ```python config = {"aws": {"region": {"primary": "us-east-1"}}}

Calling get_nested_value(config, "aws.region.primary") should return "us-east-1"

'''

def get_nested_value(data_dict: dict,key_path: str) :
    keys = key_path.split(".")
    current_location =  data_dict
    for key in keys:
        if isinstance(current_location, dict) and key in current_location:
            current_location= current_location[key]
        else:
            print(f"key {key} not found ")  
    return current_location          

if __name__ == "__main__":
    data_dict = {
        "name": {    
            "agent_settings": {
                "model_config": {
                    "llm_type": "gpt-4",
                    "parameters": {
                        "temperature": 0.7,
                        "max_tokens": 2048
                    }
                },
                "retry_policy": {
                    "max_attempts": 3
                }
            }
        }    
    }

    key_path = "agent_settings.model_config.parameters.max_tokens"

    value = get_nested_value(data_dict, key_path)

    print(value)