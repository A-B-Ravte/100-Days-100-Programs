'''
Priority-Based Task Scheduler (Agent Orchestrator Core)

📥 INPUT (Task Metadata)

You receive a list of task definitions.

Each task has:

Field	Meaning
task_id	Unique task identifier (string)
priority	Integer (lower number = higher priority)
created_at	Integer timestamp (lower = older task)

🔑 SCHEDULING RULES (READ CAREFULLY)
Rule 1️ — Priority comes first

Lower priority number = higher execution priority

Example:

priority 1 runs before priority 2

Rule 2️ — Tie-breaker: FIFO (age)

If two tasks have same priority:

Task with lower created_at runs first

This ensures:

Fairness

Deterministic behavior

No starvation

Rule 3️ — Input validation (VERY IMPORTANT)

A task is valid ONLY IF:

task_id exists and is a string

priority exists and is an integer

created_at exists and is an integer

Invalid tasks must be:

Ignored silently

Must NOT crash the scheduler

Rule 4️ — Deterministic output

Given the same input:

Output order must ALWAYS be the same

No randomness.

 EXPECTED OUTPUT (FOR GIVEN INPUT)

Input:

tasks = [
    {"task_id": "A1", "priority": 3, "created_at": 5},
    {"task_id": "A2", "priority": 1, "created_at": 1},
    {"task_id": "A3", "priority": 2, "created_at": 3},
    {"task_id": "A4", "priority": 1, "created_at": 2},
]


Output:

["A2", "A4", "A3", "A1"]
'''
import logging

logging.basicConfig(level=logging.INFO)

def schedule_tasks(tasks: list[dict]) -> list[str]:
    try:
        
        priority_base_data = {}
        for task in tasks:
            t_id, priority, created_at = task['task_id'], task['priority'], task['created_at']

            if not isinstance(t_id, str) or not isinstance(priority, int) or not isinstance(created_at, int):
                logging.info(f"Skipping Invalid Input type for task {task}")
                continue
            
            priority_base_data[priority] = priority_base_data.get(priority, {})
            priority_base_data[priority][t_id] = created_at
           
        if priority_base_data == {}:
            return []
        print(priority_base_data)
        priority_base_data = dict(sorted(priority_base_data.items(), key=lambda item: item[0], reverse=False))
        ordered_tasks = []
        for key, data in priority_base_data.items():
            data = dict(sorted(data.items(), key=lambda item: item[1], reverse=False))
            for id, v in data.items():
                ordered_tasks.append(id)
    
    except (TypeError, KeyError, ValueError) as e:
        logging.error(f"Invalid input task caught error {e}")

    return ordered_tasks

if __name__=="__main__":
    tasks = [
        {"task_id": "A1", "priority": 3, "created_at": 5},
        {"task_id": "A2", "priority": 1, "created_at": 1},
        {"task_id": "A3", "priority": 2, "created_at": 3},
        {"task_id": "A4", "priority": 1, "created_at": 2},
    ]    
    
    output = schedule_tasks(tasks)
    print(output)