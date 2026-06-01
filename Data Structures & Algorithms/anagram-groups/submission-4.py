"""
Understand: Find anagrams and group them together into sublists
Return. List of sublists
Given, array of strings
Edge case: One String with 0 lenght

Plan:
wordToAnagram = {}
for each str in strs:
    count characters
    if this signature of characters exist in wordToAnagram:
        append this str
    if not: 
        create a new sublist
return wordToAnagram.values
"""
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        wordToAnagrams = defaultdict(list)
        for word in strs:
            signature = [0] * 26
            for char in word:
                signature[ord(char) - ord('a')] += 1
            wordToAnagrams[tuple(signature)].append(word)
        return list(wordToAnagrams.values())
            


        