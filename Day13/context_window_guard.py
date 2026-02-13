'''
The "Middle-Out" Context Guard


The Problem Statement
LLMs have a finite context window. When handling long documents, you must ensure the prompt fits. However, the most important information is usually at the beginning (instructions) and the end (the specific question). Therefore, when text is too long, we perform "Middle-Out Truncation"—cutting the center while keeping the "Head" and the "Tail."

 The Rules to Apply
Token Estimation: Use the industry heuristic where 1 token≈4 characters.

Truncation Logic: If the estimated tokens exceed the max_tokens limit:

Keep the first 25% of the allowed characters.

Keep the last 25% of the allowed characters.

Replace the middle with "... [TRUNCATED] ..."

Return Type: Return a dictionary containing the processed text and metadata.

 Example Input
Parameters:

text: A very long string (e.g., 5000 characters).

max_tokens: 500 (which means 500×4=2000 characters is our limit).

Text Snippet:
"INSTRUCTIONS: Summarize the following... [thousands of words of legal text] ...END OF DOCUMENT."

 Expected Output
Resulting Dictionary:

Python
{
    "final_text": "INSTRUCTIONS: Summarize the... [TRUNCATED] ...END OF DOCUMENT.",
    "original_token_count": 1250, # (5000 / 4)
    "was_truncated": True,
    "current_token_count": 500
}

'''

def context_guard(text: str, max_tokens: int)-> dict:
    is_truncated = False
    original_token_count = len(text) / 4
    count = original_token_count
    
    while True:
        if count > max_tokens :
            head = text[0:int(count)]
            tail = text[-int(count):-1]
            truncated_text = head + tail
            count = len(truncated_text) / 4
            is_truncated = True
        else :
            break    

    if is_truncated:
        return {"final_text": truncated_text, "original_text_count":original_token_count, "was_truncated":is_truncated, "current_token_count": count}    
    else:
        return {"final_text": text, "original_text_count":original_token_count, "was_truncated":is_truncated, "current_token_count": original_token_count}        

if __name__  == "__main__":
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx"
    max_tokens = 10
    output = context_guard(text, max_tokens)
    print(output)