s = "anagram"
t = "nagaram"

if len(s) != len(t):
    print(False)
sort_s = sorted(s)
sort_t = sorted(t)
if sort_s == sort_t:
    print(True)
else:
    print(False)