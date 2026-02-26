class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val): 
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
        
    def remove_duplicates(self):
        curr = self.head
        while curr:
            if curr.prev and curr.prev.val == curr.val:
                if curr.prev == self.head:
                    curr.prev = self.head
                    self.head = curr
                else:
                    curr.prev.prev.next = curr
                    curr.prev = curr.prev.prev
            curr = curr.next
        return self.head
                
    def display(self):
        current = self.head
        while current:
            print(current.val, end=" <-> " if current.next else "\n")
            current = current.next
            
dll = DoublyLinkedList()
for value in [1, 1, 2, 3, 3, 4, 4, 4, 5]:
    dll.append(value)
print("Doubly Linked List with duplicates:")
dll.display()

dll.remove_duplicates()
print("Doubly Linked List after removing duplicates:")
dll.display()