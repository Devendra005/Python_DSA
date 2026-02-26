class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def push(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        
    def pop(self):
        if self.front is None:
            return -1
        popped = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return popped

# Example usage
queue = MyQueue()
queue.push(10)
queue.push(20)
queue.push(30)
print("Popped item:", queue.pop())
print("Popped item:", queue.pop())
print("Popped item:", queue.pop())
print("Popped item from empty queue:", queue.pop())