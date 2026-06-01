class Solution:
    def countBits(self, n: int) -> List[int]:
        # #my approach which is not efficient
        # output = []
        # for c in range(n+1):
        #     i = c
        #     res = 0
        #     while i:
        #         i &= i-1
        #         res+=1
        #     output.append(res)
        # return output

        #optimal approach
        output = [0] * (n+1) #brackets are important here
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            output[i] = 1 + output[i - offset]
        return output