'''
Sliding Window Agent Memory Counter
 REAL-WORLD CONTEXT (WHY THIS EXISTS)

In Agentic AI systems, an agent:

Receives continuous events

Cannot remember everything forever

Must focus on recent context

Examples:

Count last 10 user errors

Track last 5 tool failures

Monitor recent suspicious activities

Decide escalation based on recent pattern, not full history

This is called Sliding Window Memory.

Used in:

Fraud detection agents

LLM safety filters

Observability agents

Autonomous monitors

You are implementing a core memory primitive.

 INPUT

You receive a list of events in time order.

Each event:

{
    "event_type": str,
    "timestamp": int   # seconds
}


Example:

events = [
    {"event_type": "error", "timestamp": 1},
    {"event_type": "success", "timestamp": 2},
    {"event_type": "error", "timestamp": 3},
    {"event_type": "error", "timestamp": 6},
    {"event_type": "success", "timestamp": 7},
    {"event_type": "error", "timestamp": 9}
]

RULES

Events are sorted by timestamp (ascending)

Window is defined as:

latest_timestamp - window_size


Only include events whose timestamp is >= window_start

Ignore invalid events safely

Do NOT crash

 EXAMPLE
Input
window_size = 5


Latest timestamp = 9
Window start = 9 - 5 = 4

We include events with timestamp ≥ 4:

[
    {"event_type": "error", "timestamp": 6},
    {"event_type": "success", "timestamp": 7},
    {"event_type": "error", "timestamp": 9}
]

Expected Output
{
    "error": 2,
    "success": 1
}

 EDGE CASES YOU MUST HANDLE

Empty list → return empty dict

Invalid entries → skip

window_size <= 0 → return empty dict

'''
from typing import List, Dict
import logging

logging.basicConfig(level=logging.INFO)

def count_recent_events(events : List[Dict], window_size : int) -> Dict:

    if not events or window_size <= 0:
        return {}
    
    try:
        latest_timestamp = events[-1]['timestamp']
        if not isinstance(latest_timestamp, int):
            return {}
    except(KeyError, TypeError) as e:
        logging.error(f"Invalid event found error as {e}")    
    
    window_start = latest_timestamp - window_size
    memory_count = {}

    for event in events:
        try:
            timestamp = event['timestamp']
            event_type = event['event_type']

            if not isinstance(timestamp, int) or not isinstance(event_type, str):
                logging.info(f"Skipping Invalid event {event}")
                continue

            if timestamp>=window_start:
                memory_count[event_type] = memory_count.get(event_type, 0) + 1
        except (TypeError, ValueError, KeyError) as e:
            logging.error(f"Invalid event found error as {e}")
            continue

    return memory_count


if __name__ == "__main__":

    events = [
        {"event_type": "error", "timestamp": 1},
        {"event_type": "success", "timestamp": 2},
        {"event_type": "error", "timestamp": 3},
        {"event_type": "error", "timestamp": 6},
        {"event_type": "success", "timestamp": 7},
        {"event_type": "error", "timestamp": 9}
    ]

    memory_count = count_recent_events(events, 5)
    print(memory_count)