
"""
For each row, check if there are duplicates

For each column, check if there are duplicates

For each box check if there are duplicates
Might have to sacn the board 3 times, and its repeated work.

Could we say for each element could we find its row, column and box and check them at once if there is duplicates. This is similar to where we did the checking in a array by having a set.
Here, we could have a dictionary with 9 sets for each row, another one for 9 sets for each column and 9 sets for each box. Use the row number and column number as keys. For the box, 

00 = 0
01 = 1
02 = 2
10 = 3
11 = 4
12 = 5
20
21
22
use tuple as a key, we have 9 combinations of the ro

"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = defaultdict(set)
        colDict = defaultdict(set)
        boxDict = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                elem = board[r][c]
                if elem == ".":
                    continue
                if ((elem in rowDict[r]) or
                    (elem in colDict[c]) or
                    (elem in boxDict[(r // 3, c // 3)])):
                    print(boxDict)
                    return False
                else:
                    rowDict[r].add(elem)
                    colDict[c].add(elem)
                    boxDict[(r // 3, c // 3)].add(elem)
        return True

        