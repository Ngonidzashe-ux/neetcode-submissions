"""
Understand:
Find the number of ways in 2 way grid to move from the top left to the bottom right
Input: int m, int n. Output: int
Constraints. Can move down or right
Edge cases. One column, One row, no grid

Match: This is similar to longest commmon subsequence in that it is 2d

Plan:
Brute Force: 
Decision Tree with the nodes as coordinates, decisions left or right, terminating decision is if we go outside range and a path leading to the target is one path
Exponential time without memoization. 2 decisions at each point to include or not so 2^mn
Introducing caching so that there is no repeated work.
Bottom up approach to build from the base case and address terminating conditions

DP:
Initialise dp array
dp = [[0] * n for i in range(m)]
dp[m-1][n-1] = 1
for r in range(m-1, -1, -1):
    for c in range(n-1, -1, -1):
        if (r + 1) < m:
            dp[r][c] += dp[r+1][c] 
        if (c + 1) < n:
            dp[r][c] += dp[r][c+1] 
return dp[0][0]




"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        dp[m-1][n-1] = 1
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if (r + 1) < m:
                    dp[r][c] += dp[r+1][c] 
                if (c + 1) < n:
                    dp[r][c] += dp[r][c+1] 
        return dp[0][0]
    

        
