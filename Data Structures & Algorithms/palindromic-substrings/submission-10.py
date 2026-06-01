class Solution:
    def countSubstrings(self, s: str) -> int:
        #odd string
        res = 0
        for i in range(len(s)):
            l, r = i,i
            while l >= 0 and r < len(s):
                if not (s[l] == s[r]):
                    break
                res+=1
                l-=1
                r+=1

        #Even string
        for i in range(len(s)):
            l, r = i, i+1
            while l >= 0 and r < len(s):
                if not (s[l] == s[r]):
                    break
                res+=1
                l-=1
                r+=1
        return res

        