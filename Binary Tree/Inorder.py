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

def In_order(root, result):
    if root is None:
        return
    In_order(root.left, result)
    result.append(root.val)
    In_order(root.right, result)

result =[]
In_order(Five, result)
print(result)