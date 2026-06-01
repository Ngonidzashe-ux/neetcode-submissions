class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Initialise a 2D grid with 0 where j iterates over text2 and i for text 1
        #
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

#Iterate through the degree in reverse order:
#Start at the bottom right and making your way up
#Gonna finish the bottom row starting from the right going to the left
        for i in range(len(text1) - 1, -1, -1): #row
            for j in range(len(text2) - 1, -1, -1):#column
            #if characters are the same, then thats 1+cell diagonally below
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                #if not, you want to take the max between the value on the immediate right or immediate bottom of the current cell
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]