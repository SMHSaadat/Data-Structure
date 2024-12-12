class dNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

class CdLinekd_list:
    def __init__(self):
        self.head = None
    
    def insert_first(self, data):
        a = dNode(data)
        if self.head is None:
            self.head = a
            self.head.next = self.head
            self.head.back = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            a.next = temp.next
            temp.next.back = a
            temp.next = a
            a.back = temp
            self.head = a
    
    def insert_last(self, data):
        a = dNode(data)
        if self.head is None:
            self.head = a
            self.head.next = self.head
            self.head.back = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            a.next = self.head
            self.head.back = a
            temp.next = a 
            a.back = temp
            
    def insert_after(self, x, data):
        if self.head is None:
            print("empty")
            return None
        else:
            temp = self.head
            while temp.data != x:
                if temp.next == self.head:
                    print("your data not found")
                    return None
                else:
                    temp = temp.next
            a = dNode(data)
            a.next = temp.next
            temp.next.back = a 
            temp.next = a
            a.back = temp
        
    def delete_first(self):
        if self.head is None:
            print("empty")
            return None
        elif self.head.next == self.head:
            del(self.head)
            self.head = None
            return None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = temp.next.next
            temp.next.back = temp
            del(self.head)
            self.head = temp.next
            
    
    def delete_last(self):
        if self.head is None:
            print("empty")
            return None
        elif self.head.next == self.head:
            del(self.head)
            self.head = None
            return
        else:
            temp = self.head
            
            while temp.next.next != self.head:
                temp = temp.next
            del(temp.next)
            temp.next = self.head
            self.head.back = temp
    
    
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
        t.next.back = temp
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
            temp = self.head
            while temp.next.data != x:
                if temp.next == self.head:
                    print("your data not found")
                    return None
                temp = temp.next
            t = temp.next
            temp.next = t.next
            t.next.back = temp
            del(t)
                
    def show(self):
        if self.head is None:
            print("empty")
            return None
        else:
            temp = self.head
            while temp.next != self.head:
                print(temp.daat)
                temp = temp.next
            
