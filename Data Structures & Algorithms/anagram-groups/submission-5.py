"""
Understand:
1. Group anagrams together and then return a list of anagrams.
2. Handle edge cases: Empty list

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        anagramDict = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for char in word:
                arr[ord(char) - ord('a')] += 1
            anagramDict[tuple(arr)].append(word)
        result = [anagramDict[key] for key in anagramDict]
        return result
