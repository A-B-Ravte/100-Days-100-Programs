'''
The Problem Statement
In a GenAI lifecycle, you must dynamically build prompts by merging user data into templates. However, you cannot trust user input. You need a function that:

Injects variables into a template safely.

Handles Missing Data without raising a KeyError.

Sanitizes the input to prevent "Prompt Injection" or malicious code (like HTML tags) from being passed to the model.

 Example Input
You will receive two things: a Template String and a Payload Dictionary.

Template: "System: You are a {role}. Task: {task}. User: {user_name}."

Payload:

Python
{
    "role": "Senior AI Architect",
    "task": "Review the architecture for <script>alert('hack')</script>",
    "user_name": None  # Note: This is missing/None
}
 Expected Output
Your function should return a clean, fully-populated string:

Result: "System: You are a Senior AI Architect. Task: Review the architecture for alert('hack'). User: [Guest]."

 Requirements for your Code:
Default Values: If a key in the template is missing or None in the payload, replace it with a default value like "[Guest]" or "[Not Provided]".

Sanitization: Identify and remove common "malicious" characters or tags (specifically <script> and </script>).

Robustness: Use Python's .format() or a similar method that doesn't crash if the dictionary doesn't match the template keys perfectly.
'''
import bleach
import re
from typing import Dict

#reusable parser for each value 
def sanitize_value(value):
    if value == None:
        return "[Not Added]"
    
    clean_text = bleach.clean(str(value), tags=[], strip=True)    
           
    return clean_text.strip()    

def prompt_parser(template: str, payload: Dict)-> str :
    placeholders = re.findall(r"\{(\w+)\}", template)

    clean_mapping = {}
    for key in placeholders:
        raw_value = payload.get(key)
        clean_mapping[key] = sanitize_value(raw_value)
    
    try:
        return template.format_map(clean_mapping)
    except KeyError as e:
        # Fallback in case a placeholder didn't get caught
        return f"Error: Missing key {e} in template orchestration."

if __name__ == "__main__":
    Template = "System: You are a {role}. Task: {task}. User: {user_name}."

    Payload = {
        "role": "Senior AI Architect",
        "task": "Review the architecture for <script>alert('hack')</script>",
        "user_name": None  # Note: This is missing/None
        }
    output = prompt_parser(Template, Payload)
    print(output)