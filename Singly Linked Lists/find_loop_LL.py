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
    
    def find_loop(self):
        if self.head is None:
            return False
        
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Count the number of nodes in the loop
                slow = slow.next
                count = 1
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0

    def create_loop(self, pos):
        """Create a loop by connecting the tail to the node at index pos (0-based).
        If pos is invalid or list is empty, do nothing.
        """
        if self.head is None or pos < 0:
            return

        loop_node = None
        current = self.head
        index = 0
        # Find loop target and tail
        while current is not None:
            if index == pos:
                loop_node = current
            if current.next is None:
                tail = current
                break
            current = current.next
            index += 1
        else:
            return

        if loop_node is not None:
            tail.next = loop_node
    
    def display(self):
        curr = self.head
        seen = set()
        steps = 0
        # Prevent infinite printing if there's a loop
        while curr is not None and steps < 100:
            print(curr.val, end=" -> ")
            node_id = id(curr)
            if node_id in seen:
                print("(loop)")
                return
            seen.add(node_id)
            curr = curr.next
            steps += 1
        print("None" if curr is None else "...")

ll = SinglyLinkedList()
for v in [1,2,3,4,5]:
    ll.append(v)

# Create a loop: tail connects back to node at index 2 (value 3)
ll.create_loop(2)
print(ll.find_loop())  # prints loop length (e.g., 3)
ll.display()