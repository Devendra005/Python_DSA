s = "abcde"
goal = "deabc"

if len(s) != len(goal):
    print(False)
curr_str = s
n = len(curr_str)
for i in range (0, n):
    if curr_str == goal:
        print(True)
        break
    curr_str = curr_str[-1] + curr_str[ :-1]
print(False)


# optimal 
if len(s) != len(goal):
    print(False)
double_str = s + s
if goal in double_str:
    print(True)
else:
    print(False)