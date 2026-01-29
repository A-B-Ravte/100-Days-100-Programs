'''
Agent Task Retry Manager (Stateful Logic)
 Real-World Use Case

In agent systems:

Tools fail

APIs timeout

LLM calls fail

Retries must be controlled

Input :- 
tasks = [
    {"task_id": "T1", "status": "failed"},
    {"task_id": "T2", "status": "success"},
    {"task_id": "T1", "status": "failed"},
    {"task_id": "T3", "status": "failed"},
    {"task_id": "T1", "status": "success"},
    {"task_id": "T3", "status": "failed"},
]

Expected Output :- 

{
    "retry_count": {
        "T1": 2,
        "T3": 2
    },
    "blocked_tasks": ["T3"]
}


🔹 Rules (IMPORTANT)

Count retries only for failed attempts

If a task succeeds → stop counting further retries

If retries exceed max_retries → task is blocked

Ignore invalid task records (missing keys / wrong types)

Do NOT crash

'''

import logging

logging.basicConfig(level=logging.INFO)

def retry_summary(tasks: list[dict], max_retries: int = 2) -> dict:
    summary = {}
    summary['retry_count'] = {}
    summary['blocked_tasks'] = set()

    VALID_STATUS = ['success', "failed"]

    for task in tasks:
        try:
            status = task['status'].lower()
            id = task['task_id']
            if status not in VALID_STATUS:
                raise ValueError(f"Invalid Status '{status}' for task id {id},\nAllowed valid status is this {VALID_STATUS}")
        

            if status == "failed":
                summary['retry_count'][id] = summary['retry_count'].get(id, 0) + 1
                if summary['retry_count'][id] >= max_retries:
                    summary['blocked_tasks'].add(id)
            else:
                if id in summary['blocked_tasks']:
                    summary['blocked_tasks'].remove(id)
                logging.info(f"Task {id} is Successfully completed.") 

        except (KeyError, ValueError, TypeError) as e:
            logging.error(f"Invalid type error found as {e}")

    return summary                   
                
    

if __name__ == "__main__":
    tasks = [
        {"task_id": "T1", "status": "failed"},
        {"task_id": "T2", "status": "success"},
        {"task_id": "T1", "status": "failed"},
        {"task_id": "T3", "status": "failed"},
        {"task_id": "T1", "status": "success"},
        {"task_id": "T3", "status": "failed"},
    ]
    summary =  retry_summary(tasks)

    print(summary)
