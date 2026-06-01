class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            #left to right which is basically getting every in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top+=1

            #get every j in the right col
            for j in range(top, bottom):
                res.append(matrix[j][right-1])
            right-=1

            #This is important when we got a single row or single column
            if not (left < right and top < bottom):
                break

            for k in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][k])
            bottom-=1

            for m in range(bottom-1, top-1, -1):
                res.append(matrix[m][left])
            left+=1

        return res
    #N.B We are subtracting the bottom and right by 1 each time we use them because we know that they are out of range at the beginning






        