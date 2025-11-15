class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def append (self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next 
            current.next = new_node
    
    def traverse(self):
        if not self.head:
            print("SLL is Empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end = "-> ")
                current = current.next
            print(" ")

sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(1)
sll.traverse()