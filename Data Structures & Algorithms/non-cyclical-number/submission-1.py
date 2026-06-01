class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        if n == 1:
            return True
        while n != 1:
            res = 0
            while n:
                res += (n%10)**2
                n = n//10
            n = res
            if n == 1:
                return True
            if n in visited:
                return False
            else:
                visited.add(n)

        