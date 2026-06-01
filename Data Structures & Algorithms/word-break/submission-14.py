"""
Understand - To check if s is made up of words that are in the dictionary
Plan:
- Initialise a pointer that points to the position of s that we still need to figure out
- While the pointer is not at the end
    - For each word, check if it is the same with an equivalent portion of s starting at the current pointer
    - If yes, then break from the for loop and update current pointer to check the next portio
    - If it finished the words without matching, then return falsse
-If it gets out, then it has worked
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s)) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]


        
        