"""
Understanding:
Given daily temperatureres, can you find the number of days it took for a warmer day to appeear


Plan:
if temperatures is empty:
    return []
result = [0] * len(temperatures)
for each l in range(len(temperatures)):
    for each r in range(l + 1, len(temperatures)):
        if temperatures[r] > temperatures[l]:
            result[l] = r - l
            break


1. Create results array with 0s
2. Create an empty stack:
3. for each temperature in temperatures:
    if is smaller or equal than the last element in the stack:
        add it to the stack
    else:
        while the element is bigger:
            let element, i = stack.pop()
            results[i] = r - i


"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0] * n
        stack = []
        for r in range(n):
            temp = temperatures[r]
            if r == 0:
                stack.append((temp, 0))
            else:
                last = stack[-1][0]
                if temp <= last:
                    stack.append((temp, r))
                else:
                    while stack and temp > last:
                        last, i = stack.pop()
                        results[i] = r - i
                        if stack:
                            last = stack[-1][0]
                        else:
                            last = temp
                    stack.append((temp, r))
        return results
        