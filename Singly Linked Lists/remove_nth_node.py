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
            
    def remove_nth_from_end(self, n):
        n = 2
        slow = self.head
        fast = self.head
        for _ in range(n):
            fast = fast.next    
        if fast == None:
            return self.head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return self.head
    
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
    
sll = SinglyLinkedList()
for v in [1,3,4,7,1,2,6]:
    sll.append(v)
print("Original linked list:")
sll.display()

sll.remove_nth_from_end(2)
print("After removing 2nd node from end:")
sll.display()
              