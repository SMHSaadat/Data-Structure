class dynamci_queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            self.queue.pop(0)
        else:
            print('empty')

    def display(self):
        for i in range(len(self.queue)-1,0,-1):
            print(self.queue[i])
    
    def replace(self, old_data, new_data):
        if self.is_empty():
            print('empty')        
        for i in range(len(self.queue)):
            if self.queue[i] == old_data:
                self.queue[i] = new_data
                return
        else:
            print("your data not found")
        
    def is_empty(self):
        return len(self.queue) == 0
    
    
