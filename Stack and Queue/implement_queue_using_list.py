class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if len(self.items) == 0:
            print("dequeue from empty queue.")
            return
        x = self.items.pop(0)
        return x
    
    def front(self):
        if len(self.items) == 0:
            print("Cannot peek, queue is empty.")
            return
        return self.items[0]
    
    def rear(self):
        if len(self.items) == 0:
            print("Cannot peek rear, queue is empty.")
            return
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
queue = Queue()
queue.enqueue(23)
queue.enqueue(5)
queue.enqueue(15)
queue.enqueue(30)
print("Initial queue items:", queue.items)
print("Size:", queue.size())
print("Front:", queue.front())
print("Rear:", queue.rear())
print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
print("Front after dequeues:", queue.front())
print("Rear after dequeues:", queue.rear())
print("Is empty?:", queue.is_empty())
print("Remaining items:", queue.items)