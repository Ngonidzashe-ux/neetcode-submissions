class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Personal Attempt
        l, r = 0, (len(s1)-1)
        while r < len(s2):
            x1 = sorted(s1)
            x2 = sorted(s2[l:r+1])

            if x1 == x2:
                return True
            else:
                l+=1
                r+=1
        return False

   

        