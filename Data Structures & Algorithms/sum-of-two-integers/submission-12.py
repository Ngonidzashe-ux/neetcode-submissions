"""
Understand:
Return the sum of two integers without using the + and -
Input: int a, int b and Output int
Constraints: No + and - allowed
Edge cases: One of these things is zero right

Match:
This is similar to converting all 1s to 0s in an integer because this has to do with binary maniputlation

Plan:
Binary addition where I am adding one bit at a time

"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        aBit, bBit, cBit = 0, 0, 0
        res = 0
        for i in range(32):
            aBit = (a >> i) & 1
            bBit = (b >> i) & 1
            sBit = (aBit ^ bBit ^ cBit)
            cBit = (aBit & bBit) | (aBit & cBit) | (bBit & cBit)               
            res = res | (sBit << i) 
        if res & (1 << 31): #if the number is negative, 
            res = res - (1 << 32)
        return res

            
       
        