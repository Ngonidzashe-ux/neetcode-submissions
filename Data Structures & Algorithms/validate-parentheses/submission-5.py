class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b == '(' or b == '{' or b == '[':
                stack.append(b)
            else:
                if not stack:
                    return False
                a = stack.pop()
                if b == ')' and a != '(':
                    return False
                if b == '}' and a != '{':
                    return False
                if b == ']' and a != '[':
                    return False
                
        if stack:
            return False
        return True

        