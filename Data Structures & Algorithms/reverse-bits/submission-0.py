class Solution:
    def reverseBits(self, n: int) -> int:
        i = 31
        res = 0
        while i>=0:
            if n%2 == 1:
                res+=2**(i)
            n = n >> 1
            i-=1
        return res

        