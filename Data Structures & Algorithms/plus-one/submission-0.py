class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        for r in range(len(digits) - 1, -1, -1):
            total = carry + digits[r]
            if total >= 10:
                carry = 1
                total = total % 10
            else:
                carry = 0
            res.append(total)
        if carry:
            res.append(carry)
        res.reverse()
        return res

