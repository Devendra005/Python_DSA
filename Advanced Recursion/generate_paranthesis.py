class solution:
    def solve(self, index, total, brackets, result):
        if index >= len(brackets):
            if total == 0:
                result.append("".join(brackets))
            return
        if total > len(brackets) // 2:
            return    
        if total < 0:
            return
    
        brackets[index] ="("
        Sum = total + 1
        self.solve(index + 1, Sum, brackets, result)
    
        brackets[index] =")"
        Sum = total - 1
        self.solve(index + 1, Sum, brackets, result)
    
    def generateParanthesis(self, n):
        brackets =[""] *(n*2)
        result = []
        self.solve(0, 0, brackets, result)
        return result

sol = solution()
n = int(input("Enter a lenght of paranthesis to be generate: "))
paranthesis = sol.generateParanthesis(n)
print(paranthesis)