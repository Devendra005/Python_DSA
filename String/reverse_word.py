s = "the sky is blue"
words = s.split()
words.reverse()
result = " ".join(words)
print(result)

# using indexing
s = "the sky is blue"
for i in range(len(s)-1, -1, -1):
    print(s[i], end="")
    if s[i] == " ":
        print(" ", end="")
print()
