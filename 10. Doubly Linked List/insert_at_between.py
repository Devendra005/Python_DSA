class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_head(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert_at_between(self, val, position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return
        
        current = self.head
        count = 0
        
        while current and count < position - 1:
            current = current.next
            count += 1
            
        if current is None:
            print("Position out of bounds.")
            return
        
        new_node.next = current.next
        new_node.prev = current
        
        if current.next:
            current.next.prev = new_node
            
        current.next = new_node
        
    def display(self):
        current = self.head
        
        while current:
            print(current.val, end=" <-> " if current.next else "\n")
            current = current.next

dll = DoublyLinkedList()
dll.insert_at_head(10)
dll.insert_at_head(30)
dll.insert_at_between(20, 1)
dll.display()