"""
Understand:
efined UMPIRE with Brute-Force Decision Tree
Since the decision tree is the natural brute-force approach, I’ll integrate it into the Plan and show how DP optimizes it.

Understand
Determine if s can be segmented into words from wordDict.
Input: s: str, wordDict: List[str], Output: bool.
Edge cases: empty s, empty wordDict, single word, s not segmentable.
Constraints: 1 ≤ len(s) ≤ 200, 1 ≤ len(wordDict) ≤ 100, lowercase letters.
Intuition: Try matching words at each index, check if remainder is segmentable, optimize with DP.
Match
Like Coin Change: Decision tree of choices (coins vs. words) leading to DP.
Like Longest Common Subsequence: DP for string segmentation.
Pattern: Recursive word choices memoized into DP.
Plan
Brute-Force Decision Tree:
Root: Index i in s.
Branches: Try each word in wordDict matching s[i:i+len(word)], recurse on s[i+len(word):].
Leaf: i=len(s) (True) or no matches (False).
Issue: Exponential time due to overlapping subproblems (e.g., checking s[i:] repeatedly).
Base Case: dp[len(s)] = True (empty string is segmentable).
DP Optimization:
Initialize dp[0..len(s)] = False, dp[len(s)] = True.
For i from len(s)-1 to 0, for each word, if s[i:i+len(word)] == word, set dp[i] = dp[i + len(word)].
Break if dp[i] = True.
Handle empty wordDict and s.
Return dp[0].
Intuition Example: s="leetcode", wordDict=["leet","code"]: Tree at i=0 branches to “leet” → i=4 → “code” → i=8 (True).        
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for index in range(len(s) - 1, -1, -1):
            for word in wordDict:
                lenWord = len(word)
                if index + lenWord <= len(s) and s[index:index+lenWord] == word:
                    dp[index] = dp[index + lenWord]
                    if dp[index]:
                        break
        return dp[0]
        
        