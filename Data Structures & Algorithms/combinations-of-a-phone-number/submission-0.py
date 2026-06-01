"""
Understand:
Given digits, return all the possible combinations of the characters that they represent
Input: str, List[str]
Constraints: lowercase all of them, 2 to 9 inclusive

Plan:
if not digits:
    return []
digitMap = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], }
res = []
comb = []
def dfs(i):
    if i == len(digits):
        res.append("".join(comb.copy()))
        return
    if i > len(digits):
        return 
    for j in digitMap[digits[i]]:
        comb.append(j)
        dfs(i+1)
        comb.pop()
    d
    

"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitMap = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'],4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],6: ['m', 'n', 'o'],7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z'] }
        res = []
        comb = []
        def dfs(i):
            if i == len(digits):
                res.append("".join(comb.copy()))
                return
            if i > len(digits):
                return  
            for j in digitMap[int(digits[i])]:
                comb.append(j)
                dfs(i+1)
                comb.pop()
        dfs(0)
        return res