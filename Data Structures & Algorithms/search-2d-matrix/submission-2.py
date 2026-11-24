"""
Understand:
search for the valid row first using binary seach, then search for the valid column in there, which is the target
Plan:



"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        midRow = -1
        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                midRow = mid
                break
            elif matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1

        if midRow == -1:
            return False

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[midRow][mid] > target:
                r = mid - 1
            elif matrix[midRow][mid] < target:
                l = mid + 1
            else:
                return True
        return False

        
