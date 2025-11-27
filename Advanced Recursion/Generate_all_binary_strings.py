class solution:
    def solve(self, index, flag, numbers, result):
        if index == len(numbers):
            result.append("".join(numbers))
            return
        numbers[index] = '0'
        self.solve(index + 1, True, numbers, result)
        if flag == True:
            numbers[index] = '1'
            self.solve(index + 1, False, numbers, result)
            numbers[index] = '0'
    def generate_binary_strings(self, n):
        result = []
        numbers = [" "] * n
        self.solve(0, True, numbers, result)
        return result
    
n = input("Enter the length of binary strings: ")
n = int(n)
sol = solution()
binary_strings = sol.generate_binary_strings(n)
print(f"All binary strings of length {n} without consecutive 1s:")
print(binary_strings)
