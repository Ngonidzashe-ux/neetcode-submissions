"""
Understand:
1. If the grid is none, then return 0
2. Otherwise:
- Find number of possible unique paths to get to the bottom right
- Bottom up approach: Starting looking for possilbe unique paths starting from the end
- So we have dp[i][j] which tracks the unique paths to the tropy starting from index i, j


Plan:
1. Initialise dp array: dp = [[0 * n] for _ in range(m)]
2. The last position: dp[m-1][n-1] == 1
3. For each position, starting from last row:(i, j)
    - if i + 1 < m, then dp[i][j] += dp[i+1][j]# add the unique paths of the bottom cell
    - if i + j < n, then dp[i][j] +- dp[i][j+1] #add the unique paths of the right hand cell
Then return dp[0][0]
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        print([0] * n)
        print(dp)
        dp[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i == m - 1 and j == n -1):
                    continue
                #add the bottom
                if i + 1 < m:
                    dp[i][j] += dp[i+1][j]
                if j + 1 < n:
                    dp[i][j] += dp[i][j+1]
        return dp[0][0]
