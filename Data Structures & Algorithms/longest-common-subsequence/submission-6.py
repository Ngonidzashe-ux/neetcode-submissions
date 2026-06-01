"""
Understand:
- Find the length of the longest common subsequence between 2 strings
- Input: text1 str, text2 str. Output: int
- Edge cases: both input empty, one input empty, same input, no common letters
- Constraints: lowercase letters only

Match:
Like Unique paths, this is a 2dp problem that would benefit from a 2d matrix where
we are tracking the same characters.

Plan: 
I am not too sure what this part should be call to be honest but maybe not plan
Plan should be the pseudocode
I am breaking down this problem into smalller ones. Find the LCS between cat and crabt
C is the first and they are the saem so its 1 + LCS(at, rabt)
If the first characters is not the same, then find the max LCS. max(LCS(at, abt), LCS(t, rabt))
This is the recursive part right if you are doing top down.
Then if you are doing bottom up, then thats the dp. If they are the same, then add 1 and go down doagnoally
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
        return dp[0][0]

