class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'}': '{', ']' : '[', ')': '('}
        stack = []
        for b in s:
            if (b == '(' or b == '[' or b == '{'):
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                else:
                    opening_bracket = stack.pop()
                    print(opening_bracket)
                if hashmap[b] != opening_bracket:
                    return False
        if len(stack) != 0:
            return False
        return True

            
        