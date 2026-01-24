

class AgenticAI:
    def __init__(self, name: str):
        self.name = name
        self.memory: list[dict] = []

    def add_memory(self, task_name:str , status:str):
        record = {
            "task":task_name,
            "status":status
        }
        self.memory.append(record)
        print(f"memory added for {self.name} : {task_name}")

    def get_history(self)-> list: 
        #when you want only completed task list 
        completed = [item for item in self.memory if item['status']=='Completed']
        return completed

    def clear_memory(self):
        self.memory = []
        print(f"Memory has been clear for {self.name}")
        

if __name__ == "__main__":
    researcher = AgenticAI("Researhcer")
    history = researcher.get_history()
    print(f"History is {history}")
    researcher.add_memory("Web Search", "Started")
    
    researcher.add_memory("Open Gmail", "Started")
    
    researcher.add_memory("Web Search", "Completed")

    researcher.add_memory("Open Gmail", "Completed")
    
    history = researcher.get_history()
    print(f"History is {history}")

