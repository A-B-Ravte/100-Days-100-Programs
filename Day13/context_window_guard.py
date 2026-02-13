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
    
    char_limit = max_tokens * 4
    original_char_count = len(text)
    original_token_count = original_char_count / 4

    if original_token_count <= max_tokens:
        return {"final_text": text, "original_text_count":original_token_count, "was_truncated":False, "current_token_count": original_token_count}        

    head_size = int(char_limit * 0.25)
    tail_size = int(char_limit * 0.25)

    head_text = text[:head_size]
    tail_text = text[-tail_size:] if tail_size > 0 else ""
    filler = "... [TRUNCATED] ..."

    final_text = f"{head_text}{filler}{tail_text}" 
    
    return {
            "final_text": final_text,
            "original_token_count": original_token_count,
            "was_truncated": True,
            "current_token_count": len(final_text) / 4
        }

if __name__  == "__main__":
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx"
    max_tokens = 10
    output = context_guard(text, max_tokens)
    print(output)