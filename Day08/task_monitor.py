'''
Input Structure

You receive a list of task execution reports:

tasks = [
    {"task_id": "A1", "status": "success", "execution_time": 8},
    {"task_id": "A2", "status": "failed", "execution_time": 12},
    {"task_id": "A3", "status": "running", "execution_time": 15},
    {"task_id": "A4", "status": "success", "execution_time": 5},
    {"task_id": "A5", "status": "unknown", "execution_time": 7},
    {"task_id": "A6", "status": "success"},               # missing time
    {"task_id": "A7", "execution_time": 20},              # missing status
    {"task_id": None, "status": "success", "execution_time": 4},
]

Expected Output Structure
{
    "total_tasks": int,                 # valid tasks only
    "success": int,
    "failed": int,
    "running": int,
    "average_execution_time": float,    # only valid times
    "long_running_tasks": List[str],    # execution_time > 10
}

Valid task conditions

A task is considered valid only if:

task_id exists and is a string

status is one of:

"success", "failed", "running"

execution_time exists and is an integer

If any of these are missing or invalid:
Skip the task silently (do not crash)
'''

from typing import List, Dict
import logging

# Configure basic logging for our "Agent"
logging.basicConfig(level=logging.INFO)

VALID_STATUS = ['success', 'failed', 'running']

def summarize_tasks(tasks: List[Dict]) -> Dict:
    summary = { "total_tasks": 0, 
            "success":  0, 
            "failed": 0,
            "running":  0,
            "average_execution_time":  0, 
            "long_running_tasks":  [],
        }
    total_time = 0
    for task in tasks:
        try : 
            id = task['task_id']
            status = task['status'].lower()
            execution_time = task['execution_time']

            if not isinstance(id, str) or not isinstance(execution_time, int) or status not in VALID_STATUS :
                raise ValueError(f"Invalid Task {task}")
            
            summary['total_tasks'] += 1
            summary[status] += 1   
            total_time += execution_time

            if execution_time > 10:
                summary['long_running_tasks'].append(id)   

        except Exception as e:
            logging.error(f"Skipping invalid task {task}")    

    if summary['total_tasks'] > 0:        
        summary['average_execution_time'] = total_time / summary['total_tasks']
    
    return summary

if __name__ == "__main__":
    tasks = [
    {"task_id": "A1", "status": "success", "execution_time": 8},
    {"task_id": "A2", "status": "failed", "execution_time": 12},
    {"task_id": "A3", "status": "running", "execution_time": 15},
    {"task_id": "A4", "status": "success", "execution_time": 5},
    {"task_id": "A5", "status": "unknown", "execution_time": 7},
    {"task_id": "A6", "status": "success"},
    {"task_id": "A7", "execution_time": 20},
    {"task_id": None, "status": "success", "execution_time": 4}
    ]
    summary = summarize_tasks(tasks)
    print(summary)
