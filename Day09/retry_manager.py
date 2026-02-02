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
    retry_count = {}
    succeeded = set()

    VALID_STATUS = ['success', "failed"]

    for task in tasks:
        try:
            status = task['status'].lower()
            id = task['task_id']
            if not isinstance(id, str) or status not in VALID_STATUS:
                raise ValueError(f"Invalid status or task_id type")
        
            if id in succeeded:
                continue
            
            if status == "failed":
                retry_count[id] = retry_count.get(id, 0) + 1
                
            elif status == "success":
                succeeded.add(id)
                logging.info(f"Task {id} is Successfully completed.") 
                        
                       
        except (KeyError, ValueError, TypeError) as e:
            logging.error(f"Invalid type error found as {e}")

    final_retry_counts = {k: v for k, v in retry_count.items() if v > 0}
    
    blocked_tasks = [
        t_id for t_id, count in final_retry_counts.items()
        if count >= max_retries and t_id not in succeeded
    ]

    return {
        "retry_count": final_retry_counts,
        "blocked_tasks": blocked_tasks
    }        
    

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
