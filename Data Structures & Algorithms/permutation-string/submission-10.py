class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        if len(s1) > len(s2):
            return False

        from collections import Counter
        
        s1Count = Counter(s1)
        window = Counter(s2[:len(s1)])   # first window

        if s1Count == window:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            # add new char
            window[s2[r]] += 1
            # remove old char
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1

            if s1Count == window:
                return True
        
        return False
