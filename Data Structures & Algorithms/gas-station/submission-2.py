"""
Understand:
Given amount of gas[i] at station i and the cost[i] which is gas needed to travel from i to ith, return 
a starting point that allows complete circuit travel or return -1 if impossible
Input: List[int] gas, List[int], cost, Output = int
Constraints: Guaranteed solution existence
Edge cases: None

Plan:




"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start
                    
            
            


                
