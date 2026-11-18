"""
Implement a stack class.

Stack is a data structure such that the last element is the first element out. 
1,2,0
Push - Use array for constant time
Pop - Use array for constant time. Can track the tail index at all times and update it
Top - Track the tail index too for constant time.
Might need to keep track of a min heap for it to be easy for us to get Min since we cant do that with the array. Heap would have to be adjusted in log n time in push and pop.

Might have to have a monotonic deqeue that we update together with our stack.
Maybe just another array that tracks the minimum from the left and we just keep the tail index the same as well.

push:
        
    
    If the stack is empty:
        append val to stack
        append val to minimum
        increment tail to point to the last valid element
    
    If the stack is not empty:
        if the tail is the same index as the length of stack - 1:
            append val to stack
            check current tail and new value and update minimum
            increment tail 
        else:
            let current = minimum[tail]
            update tail
            if current > new value:
                write new value to the  tail
            else:
                write current to minimum
            write value to the stack at tail
            
    
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        self.tail = -1

    def push(self, val: int) -> None:
        nextIndex = self.tail + 1
        if nextIndex == len(self.stack):
            self.stack.append(val)
            if nextIndex == 0:
                self.minimum.append(val)
            else:
                self.minimum.append(min(self.minimum[self.tail], val))
        else:
            self.stack[nextIndex] = val
            if nextIndex == 0:
                self.minimum[nextIndex] = val
            else:
                self.minimum[nextIndex] = min(self.minimum[self.tail], val)
        self.tail = nextIndex

          
 
    def pop(self) -> None:
        self.tail -= 1
        
    
    def top(self) -> int:
        return self.stack[self.tail]
    

    def getMin(self) -> int:
        return self.minimum[self.tail]
        
