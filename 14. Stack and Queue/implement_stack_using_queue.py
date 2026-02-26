from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.queue = deque()
    
    def push (self, item):
        self.queue.append(item)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
    
    def pop(self):
        if len(self.queue) == 0:
            return "Stack is Empty."
        return self.queue.popleft()
    
    def peek(self):
        if len(self.queue) == 0:
            return "Stack is Empty."
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
S_to_Q = StackUsingQueue()
S_to_Q.push(10)
S_to_Q.push(20)
S_to_Q.push(30)
S_to_Q.push(40)
print("Initial Stack items : ",S_to_Q.queue)
print("Top Item :",S_to_Q.peek())
S_to_Q.pop()
S_to_Q.pop()
print("After poping the stack is :",S_to_Q.queue)
print("Top item :",S_to_Q.peek())
S_to_Q.push(5)
print("Added 5 to stack")
print("Top item :", S_to_Q.peek())