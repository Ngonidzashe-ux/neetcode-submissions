"""
Understand:
- Need to find a way to count and store the frequencies of each charater in each word
- Then compare those frequencies one by one

Plan:
- Initialise S and T hashmaps
- Iterate through s, and for each character in s, increment the count of the character in the hashmap
- Do the same for t
- Then go through S, comparing the value of each key to the one in T
- Return false if they are different
- Return true after everything
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        S, T = {}, {}
        for i in range(len(s)):
            S[s[i]] = 1 + S.get(s[i], 0)
            T[t[i]] = 1 + T.get(t[i], 0)
        for char in T:
            if T[char] != S.get(char, 0):
                return False
        return True

        