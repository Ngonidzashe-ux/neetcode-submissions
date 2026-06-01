"""
Valid anagram.
Sort and compare if they are the same but this is expesive, n log n at least
So use a hashmap that counts the occurence of each character for both words.
Then you can go through one hashmap, for each key character in there, extract the value and compare this with the corresponding value for the same key in the other hashmap.
The space complexity is constant time coz its only 26 and the time is n coz at most you have to go thourhg the longest 
"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sFreq = Counter(s)
        print(sFreq)
        for char in t:
            if sFreq.get(char, 0):
                sFreq[char] -= 1
            else:
                return False
            
        return True


        