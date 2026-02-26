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
        
    def delete_all_occurrences(self, key):
        if self.head.next is None and self.head.val == key:
            return None
        temp = self.head
        prev = None 
        New_head = self.head
        while temp is not None:
            if temp.val == key:
                if prev is not None:
                    prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = prev
                if temp == New_head:
                    New_head = New_head.next
            prev = temp
            temp = temp.next
        return New_head
    
    def display(self):
        current = self.head
        
        while current:
            print(current.val, end=" <-> " if current.next else "\n")
            current = current.next
            
dll = DoublyLinkedList()
for value in [2, 2, 3, 2, 10]:
    dll.append(value)    
print("Original List:")
dll.display()

dll.delete_all_occurrences(2)
print("List after deleting all occurrences of 2:")
dll.display()