class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i  == '[' or i == '{':
                stack.append(i)
                
            else:
                if not stack:
                    return False
            
                opening = stack.pop()

            if i == ')' and opening != '(':
                return False
            if i == '}' and opening != '{':
                return False
            if i == ']' and opening != '[':
                return False
            
        return not stack



        
        