nums = [1, 2, 3, 4, 5, 6, 1]

def maxScore(self, cardPoints: list[int], k: int) -> int:
    if k == len(cardPoints):
        return sum(cardPoints)
    left_sum = 0
    n = len(cardPoints)
    right_sum = 0   
    max_sum = 0
    for i in range(0, k):
        left_sum += cardPoints[i]
    max_sum = left_sum
    right_idx = n - 1
    for i in range(k - 1, -1, -1):
        left_sum -= cardPoints[i]
        right_sum += cardPoints[right_idx]
        max_sum = max(max_sum, left_sum + right_sum)
        right_idx -= 1
    return max_sum

print(maxScore(0, nums, 3))