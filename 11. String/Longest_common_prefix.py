strs = ["flowers", "flow", "flight"]

if len(strs) == 0:
    print(" ")
result = ""
base = strs[0]
for i in range(0, len(base)):
    for word in strs[i: ]:
        if i == len(word) or word[i] != base[i]:
            print(result)
    result += base[i]
print(result)