class dNode:
    def __init__(self, data):
        self.back = None
        self.data = data
        self.next = None
        
class dLinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        a = dNode(data)
        if self.head is None:
            self.head = a
            return
        
        a.next = self.head
        a.next.back = a
        self.head = a

    def insert_last(self, data):
        a = dNode(data)
        if self.head is None:
            self.head = a
            return
    
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = a
        a.back = temp

    def insert_after(self, x, data):
        if self.head is None:
            print("empty")
            return None
        
        temp = self.head
        while temp.data != x:
            if temp.next is None:
                print("your data not found")
                return None
            temp = temp.next
            
        a = dNode(data)
        if temp.next:
            a.next = temp.next
            temp.next = a
            a.back = temp
            a.next.back = a
        else:
            temp.next = a
            a.back = temp

    def delete_first(self):
        if self.head is None:
            print("empty")
            return None
        
        elif self.head.next is None:
            del(self.head)
            self.head = None
            return None
        
        temp = self.head
        self.head = self.head.next
        self.head.back = None
        del(temp)

    def delete_last(self):
        if self.head is None:
            print("empty")
            return None
        
        temp = self.head
        while temp.next != None:
            temp = temp.next
            
        temp.back.next = None
        del(temp)

    def delete_after(self, x):
        if self.head is None:
            print("empty")
            return None
        
        elif self.head.next is None:
            return
        
        temp = self.head
        while temp.data != x:
            if temp.next is None:
                print("your data not found")
                return None
            temp = temp.next
            
        temp.next = temp.next.next
        a = temp.next.back
        temp.next.back = temp
        del(a)

    def delete(self, x):
        if self.head is None:
            print("empty")
            return None
        
        elif self.head.data == x:
            a = self.head
            self.head = a.next
            self.head.back = None
            del(a)
            return None
        
        temp = self.head
        while temp.data != x:
            if temp.next is None:
                print("your data not found")
                return None
            temp = temp.next
            
        if temp.next is None:
            temp.back.next = None
            del(temp)
        else:
            temp.back.next = temp.next
            temp.next.back = temp.back
            del(temp)
    def show(self):
        if self.head is None:
            print("empty")
            return None
        elif self.head.next == self.head:
            print(self.head.data)
            return
        else:
            temp = self.head
            while temp.next != self.head:
                print(temp.data)
                temp = temp.next
            