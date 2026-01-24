'''
The Task: Write a script that takes a list of "dirty" strings (e.g., [" 100 ", "N/A", "25.5$", "30", "missing"]) and converts them into a clean list of floats.

Requirements:

Use a try-except block to handle strings that cannot be converted to numbers (like "N/A").

Use string manipulation to strip whitespace and remove currency symbols (like $).

Log a custom message for every failed conversion.

Why this matters for Agents: Agents often fail because they try to pass a string like "10% " into a math function. This teaches you to build "defensive" code.
'''
import re
import logging

# Configure basic logging for our "Agent"
logging.basicConfig(level=logging.INFO)
    

def clean_data(dirty_strings: list)-> list[float]:
    
    clean_list_of_float = []
    for item in dirty_string:
        item = str(item).strip()
        cleaned_item = re.sub(r'[^0-9.-]', '', item)
        try:
            converted = float(cleaned_item)
            clean_list_of_float.append(converted)
        except (ValueError, TypeError):
            logging.error(f"'{item}' of type {type(item)} cannot be converted to float")

    return clean_list_of_float

if __name__ == "__main__":
    dirty_string = ["aakash","1",2,3,7.5,"$","#aks","#1.5"] 
    clean_list_of_float = clean_data(dirty_string)
    print(clean_list_of_float)
    
