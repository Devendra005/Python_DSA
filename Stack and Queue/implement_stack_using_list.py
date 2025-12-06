class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if len(self.items) == 0:
            return "Cannot pop, stack is empty"
        x = self.items.pop()
        return x
    def top(self):
        if len(self.items) == 0:
            return "Stack is empty"
        return self.items[-1]
    def size(self):
        return len(self.items)
stack = Stack()
stack.push(5)
stack.push(10)
stack.pop()
stack.push(15)
print(f"Stack content: {stack}")
print(f"Popped item: {stack.pop()}")
print(f"Stack content : {stack}")
print(f"Top item after pop: {stack.top()}")
print(f"Is stack empty? : {stack.is_empty()}")