class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 0
        pali = ""
        for i in range(len(s)):
            count = 0
            #even numbers
            l, r = i, i
            while l >= 0 and r<len(s):
                if s[r] == s[l]:
                    count += (r-l+1)
                    if maxlen < count:
                        maxlen = count
                        pali = s[l:r+1]
                    
                else:
                    break
                
                r+=1
                l-=1

            #odd numbers:
            count = 0
            l, r = i, i+1
            while l >= 0 and r<len(s):
                if s[r] == s[l]:
                    count += (r-l+1)
                    if maxlen < count:
                        maxlen = count
                        pali = s[l:r+1]
                    
                else:
                    break
                
                r+=1
                l-=1
        return pali
            





        