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
    
    def find_middle(self):
        if self.head is None:
            return None
        
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

if __name__ == "__main__":
    ll = SinglyLinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll.append(val)
    
    print("Linked list:")
    ll.display()
    
    middle_node = ll.find_middle()
    if middle_node:
        print(f"Middle element: {middle_node.val}")
    else:
        print("List is empty")
    
    ll2 = SinglyLinkedList()
    for val in [1, 2, 3, 4]:
        ll2.append(val)
    
    print("\nEven length list:")
    ll2.display()
    
    middle_node2 = ll2.find_middle()
    if middle_node2:
        print(f"Middle element: {middle_node2.val}")
    else:
        print("List is empty")