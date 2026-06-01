class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) #Number of letters
        dp = [False] * (n+1) #Initialise the dp array with False values because we need to return True or False
        dp[n] = True #Initialise base case with True which is why we always have to do n+1

        #Recurrence:
        #For each index, you want to see if it can be broken down into the dictionary words
        #So for each index, you want to check if the word formed from there is going to match a dictionary word.
        #This could be made easier by checking the size of the word that is fr......
        for i in range(n-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
        