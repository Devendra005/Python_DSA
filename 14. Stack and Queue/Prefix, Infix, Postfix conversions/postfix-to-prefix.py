class solution:
    def postfixtoPrefix(self, s):
        stack = []
        
        for char in s:
            if char.isalnum():
                stack.append(char)
            else:
                
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                new_expr = f"{char}{operand1}{operand2}"
                
                stack.append(new_expr)
        return stack[-1]
    
# Example usage
s = "AB-DE+F*/"
print(solution().postfixtoPrefix(s))