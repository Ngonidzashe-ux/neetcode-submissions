"""
Understand:
Given a set of n cars, their positions and their speeds, determine the number of fleets that will arrive at the target position.

Constraints:
You cannot pass the car ahead of you, you can just catch up to it and then move at same speed.
Same time to reach the destination means on fleet

6, 3, 1, 8
8, 5, 2, 9
10, 7, 3, 10


Plan:

carFleets = 0

let order = maintain the order of the car positions
while there is a car that has not reached its destination:
    for each car that has not reached its destination starting witht the car most ahead
        let newPosition = position + speed
        if the newPosition is >= to newPosition of a car ahead:
            then update it to be the newPosition of the car ahead and take that car speed
    Then check if there is any cars that have newPosition >= target and remove them from consideration.
    increment car fleets


order = [3, 0, 1, 2]
while min(positions) < target:
    for car in order:
        if position[car] >= target:
            continue
        else:
            newPosition = position[car] + speed[char]
            if car > 0 and newPosition > position[car - 1]:
                position[car] = position[car - 1]
                speed[car] = speed[car - 1]
            else:
                position[char] = newPosition
    for r in range(len(positions)):
        if pos >= target:
            carFleet += 1
            positions
            continue



stack = []
heap = []
for i, p in enumerate(positions):
    heapq.heappush(heap, (1 * p, i))

while heap:
    stack.append(heapq.heappop(heap))

#0, 1, 4, 7
while stack:
    pos, car = stack.pop()
    newPos = pos + speed[car]


    


    
        
Official Solution:
The key idea is that we can use time of arrival to determine if there is any collision which would give us whether a pair of cars are a fleet.
stack = []
Sort the cars according to their position
for each car starting with the one most ahead:
    calculate the time it takes to reach target:
    append the time to the stack
    if there are at least 2 times in the stack:
        check if the newly added time is greater than what was in the stack:
        if yes, then pop it coz we dont need it and we deal with the one ahead
        
return the lenght of the stack coz that shows non overlapping times



"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        stack = []
        pairs.sort()
        for pos, spd in pairs[::-1]:
            time = (target - pos) / spd
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        