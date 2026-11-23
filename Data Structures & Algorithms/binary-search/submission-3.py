class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(l, r):
            if r < l:
                return -1
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
                return binarySearch(l, r)

            else:
                l = mid + 1
                return binarySearch(l, r)


        return binarySearch(0, len(nums) - 1)

        