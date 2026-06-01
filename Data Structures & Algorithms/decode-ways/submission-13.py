"""
Understand: 
- Count the number of ways that a string of numbers can be decoded
- We need to check the string in 1 or 2 digit intervals allowing us to check if the digt/digits are between 0 and 26
- Can be broken into subproblems: decode the first one or two digits and then decode the rest
- Bottom up approach, start at the end
- Have a dp array where dp[i] means the number of ways to decode the string starting from index i to the end
- Then we work our way back to the front since the front will depend on how many ways to decode the numbers at the back

"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if 1 <= int(s[i]) < 10:
                dp[i] = dp[i+1]
                print(s[i], dp[i])
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]
        print(dp)
        return dp[0]

        