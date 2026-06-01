class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        elements = set()
        for num in nums:
            elements.add(num)

        for num in nums:
            count = 0
            val = num
            while (val) in elements:
                count+=1
                val += 1
            length = max(length, count)
        return length

        