class solution:
    def precedence (self, ch):
        if ch == "+" or ch == "-":
            return 1
        if ch == "*" or ch == "/":
            return 2
        if ch == "^":
            return 3
        return 0
    
    def InfixtoPostix(self, s):
        stack = []
        result = []
        
        for char in s:
            if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
                result.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and self.precedence(stack[-1]) >= self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)
                
        while stack:
            result.append(stack.pop())
        return "".join(result)
    
# Example usage
s = "a+b*(c^d-e)"
solution_instance = solution()
print(solution_instance.InfixtoPostix(s))