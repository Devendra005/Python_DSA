arr = [(100, 20), (60, 10), (100, 50), (200, 50)]
w = 90

def fractional_knapsack(arr, w):
    arr.sort(key=lambda x: x[0]//x[1], reverse=True)
    current_weight = 0
    final_value = 0
    for i in range(0, len(arr)):
        if current_weight + arr[i][1] <= w:
            current_weight += arr[i][1]
            final_value += arr[i][0]
        else:
            remain = w - current_weight
            final_value += arr[i][0] * (remain / arr[i][1])
            break
    return final_value

print(fractional_knapsack(arr, w))
