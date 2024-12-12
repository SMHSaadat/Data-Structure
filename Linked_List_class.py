class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_first(self, x):
        a = Node(x)
        a.next = self.head
        self.head = a

    def insert_last(self, x):
        a = Node(x)
        if self.head == None:
            self.head = a
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = a

    def insert_after(self, x, data):  # insert after x
        if self.head is None:
            return
        elif self.head.next is None:
            if self.head.data == x:
                a = Node(data)
                self.head.next = a
            else:
                return None
        temp = self.head
        a = Node(data)
        while temp.data != x:
            if temp.next is None:
                print("not found")
                return
            temp = temp.next
        a.next = temp.next
        temp.next = a

    def delete_first(self):
        if self.head is None:
            print("empty")
            return
        self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            print("empty")
            return
        elif self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

    def delete_after(self, x):
        if self.head is None:  # check if empty
            print("empty")
            return
        elif not (self.head.next):  # check if only one object
            return
        temp = self.head
        while temp.data != x:
            if temp.next is None:  # check if x is not available
                return
            temp = temp.next
        if temp.next:  # check if x is the last object
            temp.next = temp.next.next

    def delete(self, x):
        if self.head is None:  # check if empty
            print("empty")
            return
        
        elif self.head.data == x:
            self.head = self.head.next
            print("done")
            return None

        elif self.head.next is None:
            return

        temp = self.head
        while temp.next.data != x:
            if temp.next.next is None:
                return
            temp = temp.next
        temp.next = temp.next.next

# Homework: add replace method to class
    def replace(self, old_data, new_data):
        if self.head is None:
            print("empty")
            return
    
        elif self.head.data == old_data:
            self.head.data = new_data
        
        temp = self.head
        while temp.data != old_data:
            if temp.next is None:
                print("your data not found!")
                return
            temp = temp.next
        temp.data = new_data
