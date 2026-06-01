class Solution:
    def getSum(self, a: int, b: int) -> int:
        cBit = 0
        res = 0
        for i in range(32):
            #Extract the bits and add them and determine carry
            aBit = a & 1
            bBit = b & 1
            curBit = aBit ^ bBit ^ cBit
            if aBit + bBit + cBit >= 2:
                cBit = 1
            else: 
                cBit = 0
            
            #Update the result
            res = res | curBit << i

            #Move on to the next bits
            a = a >> 1
            b = b >> 1
        if res & 1 << 31:
            res = res - (1 << 32)
        return res



        