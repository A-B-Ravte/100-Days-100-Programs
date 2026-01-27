'''
Program 1: Frequency Analyzer with Constraints

Problem
You are given a list of words (strings).
Return a dictionary where:

Key = word

Value = frequency

Ignore:

Empty strings

Case sensitivity (treat "AI" and "ai" as same)

Output should be sorted by frequency (descending)

Example Input

words = ["AI", "agent", "ai", "", "Agent", "python", "AI", "python"]


Expected Output

{
    'ai': 3,
    'agent': 2,
    'python': 2
}


Constraints

Do NOT use collections.Counter

Handle edge cases properly

Time complexity should be O(n)
'''
from typing import List

def analyzer(words :List[str]) -> dict :
    
    frequency = {}
    
    for word in words:
        if word == '':
            continue
        if word.lower() not in frequency.keys():
            frequency.update({word.lower():1})
        else:    
            frequency[word.lower()] = frequency[word.lower()] + 1
    sorted_frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))        

    return sorted_frequency   

words = ["AI", "agent", "ai", "", "Agent", "python", "AI", "python"]
sorted_frequency = analyzer(words)
print(sorted_frequency)
