class Solution:
    def isValid(self, s: str) -> bool:
        S = []
        CloseToOpen={')':'(', '}':'{', ']':'['}
        for i in s:
            if i == '(' or i == '{' or i == '[': #Super Important that you put the i's as many times as the things you want to compare
                S.append(i)
            else:
                if len(S) == 0:
                    return False
                else:
                    x = S.pop()
                    if x != CloseToOpen[i]:
                        return False
        if len(S) != 0:
            return False
        return True