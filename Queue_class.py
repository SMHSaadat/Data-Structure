class Queue:
    def __init__(self, limit=100):
        self.Q = [None] * limit
        self.limit = limit
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if self.rear >= self.limit-1:
            return -1
        elif self.front == -1:
            self.front= 0
            self.rear = 0
            self.Q[0] = data
        else:
            self.rear += 1
            self.Q[self.rear] = data
    
    def dequeue(self):
        if self.front == -1:
            return -1
        elif self.rear < self.front:
            return -1
        else:
            self.front += 1

    def show(self):
        for i in range(self.front, self.rear+1):
            print(self.Q[i])
            
    def replace(self, data, plcae):
        if self.place > self.front and self.place < self.rear:
            self.Q[plcae] = data
            