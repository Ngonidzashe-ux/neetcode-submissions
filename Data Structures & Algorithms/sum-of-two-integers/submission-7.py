class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0

        for i in range(32):  
            # Compute the resulting bit at this position
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            if cur_bit:
                res = res | (cur_bit << i)

        # Handling negative numbers (convert from 32-bit to Python integer)
        if res & (1 << 31):  # If the result is negative in 32-bit
            res = res - (1 << 32)

        return res

            

            
        