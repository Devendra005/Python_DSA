class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
drinks = Node("Drinks")
hot = Node("Hot")
cold = Node("Cold")
tea = Node("Tea")
coffee = Node("Coffee")
cola = Node("Cola")
fanta = Node("Fanta")

hot.left = tea
hot.right = coffee

cold.left = cola
cold.right = fanta

drinks.left = hot
drinks.right = cold

print(drinks.val)