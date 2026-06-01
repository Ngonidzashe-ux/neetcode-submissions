"""
Given a 2D matrix and a target, return true if the target is in the matrix
Constraints is the time complexity
Edge cases: Empty array


Match:
Binary Search, it is just that we are doing multiple rows


"""



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while top <= bot:
            midRow = (top + bot) // 2
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bot = midRow - 1
            else:
                break
        
        if not (top <= bot):
            return False

    
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[midRow][mid] == target:
                return True
            if matrix[midRow][mid] > target:
                r -= 1
            if matrix[midRow][mid] < target:
                l += 1
        return False

        