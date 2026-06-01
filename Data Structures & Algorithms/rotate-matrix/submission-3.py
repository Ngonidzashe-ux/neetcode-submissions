"""
Understand:
- Rotate the image in place
- Each position is rotated
- Start from the whole outside square and move inwards
- Therefore we need top, left, right and bottom to depict the boundaries
- The square is only valid if left < right, when left = right, it is square but it is one digit and therefore no need to rotate.
- But even in the big square, we still need to move from left to right in that outside square without moving the boundaries


Match:
-This is geometry problem similiar to problems like spiral matrices

Plan:
-

topleft = MATRIC[TOP][LEFT]
for r in range(left, right):
    



"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1

        while left < right:
            top, bottom = left, right

            for i in range(right - left):
                topLeft = matrix[top][left + i]

                matrix[top][left + i] = matrix[bottom - i][left] 
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right] 
                matrix[top + i][right] = topLeft
            left+=1
            right-=1



        