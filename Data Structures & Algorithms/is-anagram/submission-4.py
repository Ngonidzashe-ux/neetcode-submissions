class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        T = {}
        S = {}
        for i in s:
            S[i] = 1 + S.get(i, 0)
        for i in t:
            T[i] = 1 + T.get(i, 0)
        for i in T:
            if i not in S or T[i] != S[i]:
                return False
        return True
        





        