s = "()(())((()))"
max_depth = 0
current_depth = 0
stack = []
for brac in s:
    if brac == "(":
        current_depth += 1
        max_depth = max(max_depth,current_depth)
    elif brac == ")":
        current_depth -= 1
        stack.pop
print(max_depth)