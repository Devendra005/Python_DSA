class solution:
    def pretfixtoPostfix(self, s):
        stack = []
        
        n = len(s)
        for i in range(n-1, -1, -1):
            char = s[i]
            
            if char.isalnum():
                stack.append(char)
            else:
                
                operand1 = stack.pop()
                operand2 = stack.pop()
                
                new_expr = operand1 + operand2 + char
                
                stack.append(new_expr)
        return stack[-1]
    
# Example usage
s = "/-A*+DEF"
solution_instance = solution()
print(solution_instance.pretfixtoPostfix(s))