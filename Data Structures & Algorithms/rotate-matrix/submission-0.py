class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #Left and right pointers and boundaries

        l, r = 0, len(matrix) - 1
        while l < r:
            #We are gonna iterate through the entire row except the last element.
            #If right is 2 and l=0 and you say range(2), you gonna iterate and leave out the last column
            for i in range(r - l):
                #i is the offset that allows us to move one step at a time within the same row
                #Remember that moving the boundaries is for changing the whole square altogether but even after changing the whole square, we need to be traversing the entire first row of tha square.
                #So we start with the outer corners of the square and then we move in i step and we are gonna have a slanted square and complete that movement

                #Top and bottom pointers are gonna be the same as left and right respectively because we have a square and not a generic rectangle.
                top, bottom = l, r

                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1