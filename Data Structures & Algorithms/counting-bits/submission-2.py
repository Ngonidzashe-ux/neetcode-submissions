class Solution:
    def countBits(self, n: int) -> List[int]:
        count = [0] * (n + 1)
        for num in range(n + 1):
            index = num
            res = 0
            while num:
                res += num & 1
                num = num >> 1
            count[index] = res
        return count