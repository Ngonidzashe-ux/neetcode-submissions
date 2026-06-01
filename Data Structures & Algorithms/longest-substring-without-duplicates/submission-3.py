class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 0:
        #     return 0
        dupSet = set()
        maxLength = 0
        l, r = 0, 0
        while r < len(s):
            while s[r] in dupSet:
                dupSet.remove(s[l])
                l+=1
            dupSet.add(s[r])
            maxLength = max(maxLength, r-l+1)
            r+=1
        return maxLength

            
