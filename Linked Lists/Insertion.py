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
    
    def insert_at(self, val, position):
        if position < 0:
            raise ValueError("Position cannot be negative")
            
        new_node = Node(val)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
            
        current = self.head
        prev_node = None
        count = 0
        
        while current is not None and count < position:
            prev_node = current
            current = current.next
            count += 1
            
        if count < position:
            raise IndexError("Position out of bounds")
            
        prev_node.next = new_node
        new_node.next = current
    
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print("Original list:")
    ll.display()
    
    ll.insert_at(10, 1)
    print("After inserting 10 at position 1:")
    ll.display()
    
    ll.insert_at(0, 0)
    print("After inserting 0 at beginning:")
    ll.display()
    