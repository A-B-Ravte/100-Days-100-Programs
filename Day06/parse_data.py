'''
The Problem Statement
In Agentic AI, your agent will often receive a large, 
messy JSON response from an external API (like GitHub, Jira, or a Weather service). 
You need to write a Robust Parser that extracts specific "Actionable Data" while handling potential connection errors or missing fields.

The Use Case: "GitHub Repo Monitor"
Imagine you are building an automation that checks a list of GitHub repositories. 
You receive a simulated API response (a list of dictionaries). Your program must:

Extract & Transform: Create a new list of "Simplified Objects" containing only the repo_name, stars, and language.

Filter: Only include repositories that have more than 100 stars.

Data Integrity: If the language field is missing or null in the JSON, your code should default it to "Unknown" without crashing.

Error Simulation: Wrap the "request" in a way that handles the scenario where the "API" (the input data) is totally empty or malformed.
'''
from dataclasses import dataclass, asdict
from typing import List , Optional


@dataclass
class Repository:
    repo_name : str
    stars : int
    language : str 

    def __post_init__(self):
        if self.language == None:
            self.language = "Unknown"

def parse_repo_data(raw_response : List[dict]) -> Optional[Repository]:
    clean_repo = []

    for item in raw_response:
        try:
            repo = Repository(repo_name=item.get("full_name", "").strip(), stars=item.get("stargazers_count", 0), language=item.get("language"))

            if repo.stars > 100:
                clean_repo.append(asdict(repo))

        except Exception as e:
            print(f"Skipping the malformed response {e}")
    
    return clean_repo

if __name__ == "__main__":
    raw_api_response = [
        {"full_name": "python/cpython", "stargazers_count": 55000, "language": "C"},
        {"full_name": "agent-zero", "stargazers_count": 120, "language": None},
        {"full_name": "my-test-repo", "stargazers_count": 5, "language": "Python"},
        {"full_name": "awesome-ai", "stargazers_count": 450, "language": "TypeScript"},
        "invalid_entry" # This would cause a crash without our checks
    ]

    result = parse_repo_data(raw_api_response)
    print(f"Successfully Parsed {len(result)} Repositories:")
    for entry in result:
        print(entry)