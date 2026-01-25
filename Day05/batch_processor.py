'''
"The Batch Processor" (Program 05)? Here is the input to get started: raw_files = ["/home/user/logs/event1.json", "/data/config.yaml", "/var/log/event2.json", "/tmp/temp_data.txt", "direct_file.json"]

The Goal: Use a single List Comprehension to get: ["processed_event1.json", "processed_event2.json", "processed_direct_file.json"]

(Note: Don't forget that direct_file.json might not have a / in it—your code should handle that!)
'''

def batch_processor(raw_files:list)-> list :
    json_files = ["processed_" + file.split('/')[-1] for file in raw_files if file.rsplit('.')[-1].lower() == 'json']
    
    return json_files        

if __name__ == "__main__":
    raw_files = ["/home/user/logs/event1.json", "/data/config.yaml", "/var/log/event2.json", "/tmp/temp_data.txt", "direct_file.json"]
    json_files = batch_processor(raw_files)

    print(json_files)
