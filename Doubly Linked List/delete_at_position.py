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
        
    def delete_head(self):
        if self.head is None:
            print("List is empty. No head to delete.")
            return 
        
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
    def delete_by_position(self,position):
        if self.head is None:
            print("List is empty. No node to delete.")
            return
        
        if position == 0:
            self.delete_head()
            return

        curr = self.head
        count = 0
        
        while curr and count < position:
            curr = curr.next
            count += 1
            
        if curr is None:
            print("Position out of bounds.")
            return
        
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
    
    def display(self):
        current = self.head
        
        while current:
            print(current.val, end=" <-> " if current.next else "\n")
            current = current.next
            
dll = DoublyLinkedList()
dll.insert_at_head(10)
dll.insert_at_head(30)
dll.insert_at_between(20, 1)
print("Original List:")
dll.display()

dll.delete_by_position(2)
print("List after deleting node at position 2:")
dll.display()