"""
Understand:
- Longest common subsequent between two words
- cat and crabt
- compare characters at current index i.e c and c
- If its the same, increment lengthand move on to the next indices in both words
- compare a and r, not the same, so, keep a(one index stationary) and compare with next indices, abt and return the longest
- compare r, the other index is now stationary with t and return the longest, 
- Thus for the current position, index 2, the longest is the maximum from either
- Then

"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1) + 1, len(text2) + 1
        dp = [[0] * n for _ in range(m)]
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])
        print(dp)
        return dp[0][0]
