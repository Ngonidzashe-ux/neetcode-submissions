class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1  # Base case: one way to decode an empty string
        
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0  # '0' cannot be decoded by itself
            else:
                # Single digit decode is valid
                dp[i] = dp[i+1]
                # Check if a valid two-digit decode is possible
                if i + 1 < n and "10" <= s[i:i+2] <= "26":
                    dp[i] += dp[i+2]
        
        return dp[0]

        