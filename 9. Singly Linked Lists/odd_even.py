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
            
    def odd_even(self):
        if self.head is None or self.head.next is None:
            return self.head
        odd = self.head
        even = self.head.next
        even_head = even
        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return self.head
    
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
        
sll = SinglyLinkedList()
for v in [8,7,1,5,6,4,9]:
    sll.append(v)
print("Original linked list:")
sll.display()

sll.odd_even()
print("After rearranging odd and even nodes:")
sll.display()
