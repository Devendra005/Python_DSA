s = "abcabcbb"

#Brute Force Solution
def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    maxen = 0
    for i in range(0, len(s)):
        set = {}
        for j in range(i, len(s)):
            if s[j] in set:
                break
            set[s[j]] = 1
            maxen = max(maxen, j - i + 1)
    return maxen
print(lengthOfLongestSubstring(s))


#Optimal Solution
def lengthOfLongestSubstring(s: str) -> int:
    hashmap = dict()
    left = 0
    right = 0
    length = 0
    n = len(s)
    while right < n:
        if s[right] in hashmap:
            left = max(hashmap[s[right]] + 1, left)
        hashmap[s[right]] = right
        length = max(length, right - left + 1)
        right += 1
    return length
print(lengthOfLongestSubstring(s))