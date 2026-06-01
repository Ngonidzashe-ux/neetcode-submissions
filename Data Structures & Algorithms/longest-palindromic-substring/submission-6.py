class Solution:
    def longestPalindrome(self, s: str) -> str:
        #odd
        max_length = 0
        longest = ""
        for i in range(len(s)):
            l, r = i,i
            while l >= 0 and r < len(s):
                if not (s[l] == s[r]):
                    break
                if r-l+1 > max_length:
                    max_length = r-l+1
                    longest = s[l:r+1]
                l-=1
                r+=1
        #even
        for i in range(len(s)):
            l, r = i,i+1
            while l >= 0 and r < len(s):
                if not (s[l] == s[r]):
                    break
                if r-l+1 > max_length:
                    max_length = r-l+1
                    longest = s[l:r+1]
                l-=1
                r+=1
        return longest
                



        