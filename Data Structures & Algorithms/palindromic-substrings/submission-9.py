class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            #odd
            l, r = i, i
            while l>=0 and r < len(s):
                if s[l] == s[r]:
                    res+=1
                #Need a break if this is not the case
                else:
                    break
                l-=1
                r+=1

            #even
            l, r = i, i+1
            while l>=0 and r < len(s):
                if  s[l] == s[r]:

                    res+=1
                else:
                    break
                l-=1
                r+=1
        return res


        