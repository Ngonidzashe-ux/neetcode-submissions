class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, (len(s) - 1)
        while l < r:
            while l < r and not (s[l].isalnum()):
                l+=1 #You are making changes to l so the condition l<r should be checked in the while loop to ensure that the changes dont go beyond their bounds
            while l < r and not (s[r].isalnum()):
                r-=1 #You need to check the bounds and condition here too
            if s[l].lower() != s[r].lower():
                return False # Don't forget the lower part. 
            #after everything is done, you need to move the pointers for the next comparison
            l+=1
            r-=1

        return True


        