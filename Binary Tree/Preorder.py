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
Eight = Node("Eight")
Nine = Node("Nine")
Ten = Node("Ten")

Five.left = Three
Five.right = Four

Three.left = Two
Three.right = Nine

Four.left = Eight
Four.right = Ten

Eight.left = One
Eight.right = Six

def pre_order_traversal(root, result):
    if root is None:
        return
    print(root.val)
    result.append(root.val)
    pre_order_traversal(root.left, result)
    pre_order_traversal(root.right, result)

result =[]
pre_order_traversal(Five, result)
print(result)