class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if i+2 < len(dp):
                if '1' <= s[i] <= '9':
                    dp[i] = dp[i+1]
                if '10' <= s[i:i+2] <= '26':
                    dp[i] += dp[i+2]
            else:
                if '1' <= s[i] <= '9':
                    dp[i] = dp[i+1]
            
        return dp[0]



        