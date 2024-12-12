class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        a = Node(data)
        if self.head is None:
            self.head = a
            a.next = self.head 
            return
        
        a.next = self.head
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = a
        self.head = a

    def insert_last(self, data):
        a = Node(data)
        
        if self.head is None:
            self.head = a
            a.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = a
        a.next = self.head

    def insert_after(self, x, data):
        if self.head is None:
            print("empty")
            return
        
        temp = self.head
        while temp.data != x:
            if temp.next == self.head:
                print("your data not found")
                return
            temp = temp.next
            
        a = Node(data)
        a.next = temp.next
        temp.next = a

    def delete_first(self):
        if self.head is None:
            print("empty")
            return None
        
        elif self.head.next == self.head:
            del (self.head)
            self.head = None
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
            
        temp.next = temp.next.next
        del(self.head)
        self.head = temp.next

    def delete_last(self):
        if self.head is None:
            print("empty")
            return None
        
        elif self.head.next == self.head:
            del(self.head)
            self.head = None
            return None

        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        del(temp.next)
        temp.next = self.head

    def delete_after(self, x):
        if self.head is None:
            print("empty")
            return None
        
        temp = self.head
        while temp.data != x:
            if temp.next == self.head:
                print("your data not found")
                return
            temp = temp.next
        t = temp.next
        temp.next = t.next
        del(t)

    def delete(self, x):
        if self.head is None:
            print("empty")
            return None

        elif self.head.next == self.head:
            if self.head.data == x:
                del(self.head)
                self.head = None
                return
            else:
                print("your data not found")
                return
            
        temp = self.head
        while temp.next.data != x:
            if temp.next == self.head:
                print("your data not found")
                return None
            temp = temp.next
            
        t = temp.next
        temp.next = t.next
        del(t)

# Homework: write replace method
    def replace(self, old_data, new_data):
        if self.head is None:
            print("empty")
            return None
        temp = self.head
        while temp.data != old_data:
            if temp.next == self.head:
                print("your data not found")
                return None
            temp = temp.next
        temp.data = new_data
