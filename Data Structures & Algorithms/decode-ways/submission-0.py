class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1} #Store our base case. The length of the string should map to one because if we are given an empty string, we want to return 1.


        def dfs(i):#recursive function. The position we are at
            if i in dp:#if i is in our dp which means it has either been cached or i is the last position in the string in which case thats our base case
                return dp[i]
            if s[i] == "0": #if its not the end of the string and if the string is starting with zero, then thats invalid
                return 0
            
            #if its not zero, then it means its between 1 and 9, then we can take this value as a single digit
            res = dfs(i + 1)
            #for the double digit, we want to check if we have a second character coming after this first one and either the s[i] == 1, then we can make a double digit or if s[i]==2 and the second digit must be between 0 and 6
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                #add the result of the subproblem
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)

# Dynamic Programming solution
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         dp = {len(s): 1}
#         for i in range(len(s) - 1, -1, -1):
#             if s[i] == "0":
#                 dp[i] = 0
#             else:
#                 dp[i] = dp[i + 1]

#             if i + 1 < len(s) and (
#                 s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
#             ):
#                 dp[i] += dp[i + 2]
#         return dp[0]
        