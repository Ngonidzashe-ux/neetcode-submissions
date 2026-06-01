"""
Understand:
Implement a stack class with various methods
Constraints. Constant time operations for all methods
Match: Design a time based key store thing. Similar because it was a class too.
Plan:
Hashmap or Array.
"""



class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        curMin = min(val, self.minStack[-1] if self.minStack else float("inf"))
        self.minStack.append(curMin)

        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

        
