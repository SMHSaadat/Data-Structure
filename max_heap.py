class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def heapify_down_up(self, index):
        parent = self.parent(index)
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self.parent(index)

    def heapify_up_down(self, index):
        n = len(self.heap)
        largest = index
        left = self.left(index)
        right = self.right(index)

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left

        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_up_down(largest)

    def insert(self, key):
        self.heap.append(key)  
        self.heapify_down_up(len(self.heap) - 1)  

    def delete_root(self):
        if len(self.heap) != 0:
                

            root = self.heap[0]

            self.heap[0] = self.heap[-1]
            self.heap.pop()  

            if self.heap:
                self.heapify_up_down(0)

            return root
    
    def delete(self, x):
        if x in self.heap:
            index = self.heap.index(x)
            removed_element = self.heap[index]
            self.heap[index] = self.heap[-1]
            self.heap.pop()  

            if index < len(self.heap):
                self.heapify_up_down(index)
                self.heapify_down_up(index)

            return removed_element

    def display(self):
        print(self.heap)
        
    def count_leafs(self):
        result = list()
        for i in range(len(self.heap)):
            if self.left(i) > len(self.heap)-1:
                result.append(i)
        return len(result)
        

def heap_sort(elements):
    heap = MaxHeap()

    for element in elements:
        heap.insert(element)

    sorted_list = []
    while heap.heap:
        sorted_list.append(heap.delete_root())

    return sorted_list[::-1]



a = MaxHeap()

a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
a.insert(6)
a.insert(7)
a.count_leafs()
a.display()



class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2
            
def maxheap_to_minheap(max_heap):
    min_heap = MinHeap()
    for element in max_heap.heap:
        min_heap.insert(element)

    return min_heap.heap


def make_max_heap(list):
    result = MaxHeap()
    for i in list:
        result.insert(i)
    return result.heap


print(make_max_heap([5,50,30,32,25,10,20]))