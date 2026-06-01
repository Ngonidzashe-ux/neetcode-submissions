class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        closeToOpen = {'}': '{', ')': '(', ']': '[' }
        stack = []
        for br in s:
            if br == '(' or br == '{' or br == '[':
                stack.append(br)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if opening != closeToOpen[br]:
                    return False
        if stack:
            return False
        return True
        

        