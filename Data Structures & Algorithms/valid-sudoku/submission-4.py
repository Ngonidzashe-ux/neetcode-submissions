"""
Understand: Given a sodoku board, determine if its valid or not
Input: List of list with strings or row and column
Output: Bool
Edge cases: Board can never be empty

Match: This is similar to dupset where you are trying to find if there any duplicated numbers
Used a set for that coz its O(1). if its not in the set, put in the set, if its there, then return invalid

Plan:
For each row, have a set
For each col, have a set
Fore each 3*3, have a set

Each set can have a max of 9 elements
Space = O(81) constant
There is an upper bound here

for each soduku entry
if its not '.':
    check if its in the row set or col set or box set
        if not, add it
    if it is, then return invalid sodocuk
"""

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return True
        rowDict = defaultdict(set)
        colDict = defaultdict(set)
        boxDict = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                digit = board[r][c]
                if digit != ".":
                    if (digit in rowDict.get(r, set()) or
                        digit in colDict.get(c, set()) or
                        digit in boxDict.get((r//3, c//3), set())
                    ):
                        return False
                    else:
                        rowDict[r].add(digit)
                        colDict[c].add(digit)
                        boxDict[(r//3, c//3)].add(digit)

                else:
                    continue
        return True

        