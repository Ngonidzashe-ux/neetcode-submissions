"""
Understand:
Return true if you can break down s to be a list of space seperated words from the word dict
Input: s: str, wordDict: List and Output = bool
Constraints: can reuse the words from the dictionary as many times. 1 <= s.length <= 200
1 <= wordDict.length <= 100
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
Edge case: Empty wordDict, empty s, one word in dict


Match: Dont have any matching algorithm

Plan:
dp = [False] * (len(s) + 1)
dp[len(s)] = True
for each index in range(len(s) - 1, -1, -1):
    for each word in wordDict:
        lenWord = len(word)
        if index + lenWord <= len(s) and s[i:i+lenWord] == word:
            dp[index] = dp[index + lenWord]
            if dp[index]:
                break
return dp[0]

            
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
        
        