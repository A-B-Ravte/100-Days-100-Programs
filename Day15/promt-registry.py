'''
we will be building and maintain a promt registry

'''
import logging

logging.basicConfig(level=logging.INFO)

prompt_registry={}

def add_prompt(version_id: str, text: str, model_type: str, overwrite: bool = False):
    
    if not isinstance(version_id, str) or not version_id:
        logging.info(f"{version_id} must be string or not Empty")
        return
        
    if prompt_registry.get(version_id) is not None and not overwrite:
            logging.info(f"Error: {version_id} already exists. Use overwrite=True to modify.")
    else:    
        prompt_registry[version_id] = {"text":text, "model":model_type}  
    
def get_prompt(version_id: str)-> dict:
    try:   
        return prompt_registry[version_id]
    except KeyError:
        logging.info(f"{version_id} is not available")   

if __name__ == "__main__":
    add_prompt(version_id=1, text="Summarize this: {text}", model_type="gpt-4")
    add_prompt(version_id="v1.0", text="Shorten this: {text}", model_type="gpt-3.5")
    add_prompt(version_id="v1.0", text="Shorten this: {text}", model_type="gpt-3.5", overwrite=True)
    prompt =get_prompt("v1.0")
    print(prompt)