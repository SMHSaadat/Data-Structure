class dynamci_queue:
    def __init__(self, limit=10):
        self.limit = limit
        self.queue = []
    
    def enqueue(self, data):
        if len(self.queue) > self.limit:
            print('full')
            return
        self.queue.append(data)
        self.limit+=1
    
    def dequeue(self):
        if not self.is_empty():
            self.queue.pop(0)
            self.limit -= 1
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
    
    
