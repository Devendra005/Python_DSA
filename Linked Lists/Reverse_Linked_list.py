class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
            
    def reverse(self):
        if self.head is None or self.head.next is None:
            return
        
        prev = None
        current = self.head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
            
    def display(self):
        """Display the linked list"""
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
    ll.append(4)
    
    print("Original list:")
    ll.display()
    
    ll.reverse()
    print("Reversed list:")
    ll.display()
    
    ll2 = SinglyLinkedList()
    print("\nEmpty list:")
    ll2.display()
    ll2.reverse()
    print("After reverse:")
    ll2.display()          