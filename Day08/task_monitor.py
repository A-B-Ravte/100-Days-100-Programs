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

def summarize_tasks(tasks: List[Dict]) -> Dict:
    summary = { "total_tasks": 0, 
            "success":  0, 
            "failed": 0,
            "running":  0,
            "average_execution_time":  0, 
            "long_running_tasks":  [],
        }
    
    for task in tasks:
        if "task_id" not in task or "status" not in task or "execution_time" not in task:
            logging.info(f"{task} is invalid")
            continue
        if not isinstance(task['task_id'], str):
            logging.info(f"Invalid type of task_id for {task}, It should be string only.")
            continue
        if not isinstance(task['execution_time'], int):
            logging.info(f"Invalid type of execution_time for {task}, It should be integer only")
            continue
        #print(f'task status is {task["status"]}')
        if task['status'].lower() not in ["success", "failed", "running"]:
            logging.info(f"Invalid status of {task}, Status must be one of this ['success', 'failed', 'running']")
            continue
        
        summary['total_tasks'] = summary.get('total_tasks') + 1

        if task['status'] == 'success':
            summary['success'] = summary.get('success') + 1   

        if task['status'] == 'failed':
            summary['failed'] = summary.get('failed') + 1    

        if task['status'] == 'running':
            summary['running'] = summary.get('running') + 1   

        if task['execution_time'] > 10:
            summary['long_running_tasks'].append(task['task_id'])   

        summary['average_execution_time'] = summary.get('average_execution_time') + task['execution_time']
    if tasks:        
        summary['average_execution_time'] = summary['average_execution_time'] / summary['total_tasks']
    
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
