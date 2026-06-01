"""
Understand:
Given hand[i], value on card i and groupSize, return true if each group can have a consecutive numbers
Input: hand[i], groupSize and Output: bool
Edge cases: len(hand) not divisible by 4, empty hand, invalid groupsize
Constraints: len(hand) always divisible by 4.

Match:
Find the frequencies
Sort
find the next in the group by decrementing the frequencies
Find the next minimum


"""


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = {}
        for num in hand:
            freq[num] = freq.get(num, 0) + 1
        print(freq)
        hand.sort()
        for num in hand:
            if freq[num]:
                for i in range(num, num + groupSize):
                    if not freq.get(i, 0): 
                        return False
                    freq[i] -= 1
        return True

