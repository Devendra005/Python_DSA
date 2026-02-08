class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class MyStack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if self.top is None:
            return -1
        popped = self.top.data
        self.top = self.top.next
        return popped
    
# Example usage
stack = MyStack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Popped item:", stack.pop())
print("Popped item:", stack.pop())
print("Popped item:", stack.pop())
print("Popped item from empty stack:", stack.pop())