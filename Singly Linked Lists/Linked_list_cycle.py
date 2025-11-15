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
        
    def linkedListCycle(self, head):
        temp = head 
        my_set = set()
        while temp is not None:
            if temp in my_set:
                return True
            my_set.add(temp)
            temp = temp.next
        return False
    
ll = SinglyLinkedList()
for v in [1,2,3,4,5]:
    ll.append(v)

print("Linked list without cycle:")
print(ll.linkedListCycle(ll.head)) 
curr = ll.head
while curr.next is not None:
    curr = curr.next
curr.next = ll.head.next

print("Linked list with cycle:")    
print(ll.linkedListCycle(ll.head))