"""
Refined UMPIRE with Decision Tree
To emphasize the decision tree and connect it to DP:

Understand
Find fewest coins to make amount from denominations.
Input: coins: List[int], amount: int, Output: int (-1 if impossible).
Edge cases: amount=0 → 0, empty coins, no solution, single coin.
Constraints: Coins positive, unlimited use, 0 ≤ amount ≤ 10^4.
Intuition: Explore coin choices as a decision tree, optimize with DP.

Match
Like 0/1 Knapsack: Optimal choices for resource allocation.
Like Climbing Stairs: DP for subproblem summation.
Pattern: Decision tree of coin choices, memoized into bottom-up DP.

Plan
Decision Tree:
Root: Current amount.
Branches: Pick coin c, reduce to amount - c.
Leaf: amount = 0 (0 coins).
Goal: Shortest path (fewest coins).
Base Case: dp[0] = 0 (no coins for amount 0).
Memoization: dp[amt] stores minimum coins for amount amt.
Bottom-Up DP:
Initialize dp[0..amount] = amount + 1, dp[0] = 0.
For each amt from 1 to amount, for each coin c, if amt >= c, set dp[amt] = min(dp[amt], 1 + dp[amt - c]).
Return dp[amount] if < amount + 1, else -1.


Base Case: When the amount is 0, no coins are needed (dp[0] = 0).
Memoization: Store results of subproblems (e.g., dp[amt - c]) to avoid recomputing.
Bottom-Up DP: Convert the recursive tree into an iterative solution with dp array updates.

Decision Tree Visualization:
Root: Current amount (e.g., amount = 11, coins = [1, 2, 5]).
Branches: Choose a coin (1, 2, or 5), reducing the amount (e.g., 11 - 1 = 10, 11 - 2 = 9, 11 - 5 = 6).
Leaf: Reach amount = 0 (base case, 0 coins needed).
Goal: Find the path with the fewest coins (shortest path in terms of coin count).
Example: For amount = 11:
Path: Pick 5 → 6, pick 5 → 1, pick 1 → 0 (3 coins).
Path: Pick 2 → 9, pick 2 → 7, etc. (longer paths).
From Tree to DP:
Recursive: At each amount, try all coins, take minimum: f(amt) = min(1 + f(amt - c)) for all c.
Base Case: f(0) = 0, impossible amounts = infinity.
Memoization: Store f(amt) in dp[amt] to avoid recomputing.
Bottom-Up: Iterate amounts from 1 to amount, update dp[amt] using coins, collapsing the tree into a linear array.
"""



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for amt in range(amount + 1):
            for c in coins:
                if amt >= c:
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])
        return dp[amount] if dp[amount] < (amount + 1) else -1
        
        