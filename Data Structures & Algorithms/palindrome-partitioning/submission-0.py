"""
Understand:
Return the partitions of a given string in which all the partitions are substrings.
Input: s, Output: List[List[int]]
Edge cases: empty s
Constraints have to palindromes

Plan:
if not s:
    return s
Create every single way we can partition this.
The check if the partition lead to a palindrome
For something like aab, we have 3 choices
A branch with a, aa, aab. If the branch is not palindrome, we have to return 

"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        res = []
        part = []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res

      
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True      
            
             
            

        