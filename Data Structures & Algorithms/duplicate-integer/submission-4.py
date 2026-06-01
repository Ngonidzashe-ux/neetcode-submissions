class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupSet = set()
        for n in nums:
            if n in dupSet:
                return True
            dupSet.add(n)
        return False