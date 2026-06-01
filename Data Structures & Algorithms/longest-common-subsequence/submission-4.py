class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n= len(text1)+1, len(text2)+1
        dp = [([0]*n) for _ in range(m)]
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                if (text1[r] == text2[c]):
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])
        return dp[0][0]