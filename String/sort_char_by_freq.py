s = "tree"
result = ""
hash_map = {}
for ch in s:
    hash_map[ch] = hash_map.get(ch, 0) + 1
sort_char = sorted(hash_map.items(),key=lambda x:x[1], reverse=True)
for ch, freq in sort_char:
    result = result + ( ch * freq) 
print(result)