class  Node:
    def __init__(self,val):
        self.val = val
        self.next = None

node1 = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(25)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

print(node4.val)