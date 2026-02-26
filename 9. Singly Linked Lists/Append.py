class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")


ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()