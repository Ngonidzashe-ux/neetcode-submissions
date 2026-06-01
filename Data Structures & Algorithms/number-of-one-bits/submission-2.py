"""
Plan:
1. While n is non zero
2. Get the remainder from dividing it by 2, increment the number of ones if its 1
3. Then update n be the quotient after the division


"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n = n >> 1
        return res
        