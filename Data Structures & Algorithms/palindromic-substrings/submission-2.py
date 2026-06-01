class Solution:
    def countSubstrings(self, s: str) -> int:
        numPali = 0
        for i in range(len(s)):
            #odd case
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                numPali +=1
                l-=1
                r+=1
            

            #even case
            l, r = i,i+1
            while l>=0 and r < len(s) and s[l] == s[r]:
                numPali+=1
                l-=1
                r+=1
        return numPali
        

