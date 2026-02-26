from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
One = Node("One")
Two = Node("Two")
Three = Node("Three")
Four = Node("Four")
Five = Node("Five")
Six = Node("Six")
Seven = Node("Seven")

One.left = Two
One.right = Three

Two.left = Four
Two.right = Five

Three.left = Six
Three.right = Seven

def level_order_traversal(root):
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return result

result = level_order_traversal(One)
print(result)