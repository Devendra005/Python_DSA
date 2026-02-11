class solution:
    def pretfixtoInfix(self, s):
        stack = []
        
        for char in s[::-1]:
            if char.isalnum():
                stack.append(char)
            else:
                
                operand1 = stack.pop()
                operand2 = stack.pop()
                
                new_expr = f"({operand1}{char}{operand2})"
                
                stack.append(new_expr)
        return stack[-1]
    
# Example usage
s = "*+PQ-MN"
solution_instance = solution()
print(solution_instance.pretfixtoInfix(s))