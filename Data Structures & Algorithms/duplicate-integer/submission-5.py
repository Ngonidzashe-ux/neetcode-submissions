"""

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        dupSet = set()
        for num in nums:
            if num in dupSet:
                return True
            else:
                dupSet.add(num)
        return False
        