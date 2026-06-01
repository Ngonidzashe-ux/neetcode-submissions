class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #initialize all indices with False
        dp = [False] * (len(s) + 1)
        #Set the index just after the word to True
        dp[len(s)] = True

        #Iterate through the word from the last character and i is basically the starting index of the word you are trying to compare
        for i in range(len(s) - 1, -1, -1):
            #For each index, iterate through the words in the dict
            for w in wordDict:
                #Lets look at the neetcode example: len(neetcode) = 7
                #If the index i + len(neet) <= 7 which means the length of the word w is equal to the length of the word formed from starting at index i 
                #and if the word matches, then update the value of dp[i] based on the below equation that we have seen to work
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                #If there is one match with a word, then stop checking matches with other words coz thats already good enough and thats it.
                if dp[i]:
                    break

        return dp[0]