"""
Understand:
- For each character, make it the center of the substring
- Use two pointers, l and r that start from center and move outwards
- At each step, check if the l and r are pointing to the same character
- Break if not and record the substring


Plan:
- Odd:
- For i in range(len(s)):
- l , r = i, i
while l >= 0 and r < len(s):
    if s

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r - l + 1 > length:
                        res = s[l:r+1]
                        length = r - l + 1
                    l-=1
                    r+=1

                else:
                    break
        for i in range(len(s)):
            l, r = i, i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r - l + 1 > length:
                        res = s[l:r+1]
                        length = r - l + 1
                    l-=1
                    r+=1

                else:
                    break
        return res

                    
        