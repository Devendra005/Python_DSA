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
        
    def find_pairs_with_sum(self, target_sum):
        result = [ ]
        left = self.head
        right = self.head
        while right.next:
            right = right.next
        while left is not None and right is not None and left.val < right.val:
            total = left.val + right.val
            if total == target_sum:
                result.append([left.val, right.val])
                left = left.next
                right = right.prev
            elif total > target_sum:
                right = right.prev
            else:
                left = left.next
        return result
    
    def display(self):
        current = self.head
        while current:
            print(current.val, end=" <-> " if current.next else "\n")
            current = current.next
            
dll = DoublyLinkedList()
for value in [1, 2, 4, 5, 6, 8, 9]:
    dll.append(value)
print("Doubly Linked List:")
dll.display()

dll.find_pairs_with_sum(7)
pairs = dll.find_pairs_with_sum(7)
print("Pairs with sum 7:")
print(pairs)