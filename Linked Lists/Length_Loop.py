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
            
    def length(self):
        temp = self.head
        traval = 0
        my_dict = {}
        while temp is not None:
            if temp in my_dict:
                return traval - my_dict[temp]
            my_dict[temp] = traval
            traval += 1
            temp = temp.next
        return traval
    
ll = SinglyLinkedList()
for v in [1,2,3,4,5,6,7,8,9,10]:
    ll.append(v)
    
print("Length of linked list without loop:")
print(ll.length())
curr = ll.head
while curr.next is not None:
    curr = curr.next
curr.next = ll.head.next.next.next

print("Length of linked list with loop:")    
print(ll.length())
