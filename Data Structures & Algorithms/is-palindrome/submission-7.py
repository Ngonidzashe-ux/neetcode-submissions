
"""
while l < r:
    while s[l] is not alphanumeric:
        l++
    while s[r] is not alphanumeri:
        r--
    if (s[r]lower != s[l].lower)
    return false

    return true
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while (l < r):
            while (l < r and not s[l].isalnum()):
                l+=1
            while (l < r and not s[r].isalnum()):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
                   