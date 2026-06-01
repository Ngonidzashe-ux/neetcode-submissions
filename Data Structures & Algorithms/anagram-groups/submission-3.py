"""
Understand: 
1. We need to count the occurences of the characters in each string
2. Need to have the count be the key in a dict
3. Dict should have lists as values
4. Append the word to the right list depending on the count 
5. Return the values

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        res = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()
            
            
        