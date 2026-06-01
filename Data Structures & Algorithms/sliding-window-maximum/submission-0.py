"""
Refined UMPIRE
To incorporate the brute-force approach (no decision tree) and clarify the deque logic:

Understand
Return list of maximums in each sliding window of size k in nums.
Input: nums: List[int], k: int, Output: List[int].
Edge cases: nums=[], k=0, k=1, k > len(nums), all same numbers.
Constraints: 1 ≤ k ≤ len(nums) ≤ 10^5, -10^4 ≤ nums[i] ≤ 10^4.
Intuition: Track maximums in a window using a deque of decreasing indices.
Match
Like Longest Substring with At Most K Distinct Characters: Sliding window with efficient tracking.
Like Minimum Window Substring (your recent question): Window-based processing.
Pattern: Sliding window with deque for monotonic property.
Plan
Brute-Force: For each window of size k, compute max (O(n * k)).
Optimized Approach:
Use deque to store indices of potential maximums in decreasing order.
For each r:
Pop back if nums[r] > nums[q[-1]] (smaller elements can’t be maximum).
Append r to deque.
Pop front if q[0] < l (out of window).
If window size is k (r + 1 >= k), append nums[q[0]] to result, increment l.
Handle edge cases: nums=[], k=0, k > len(nums) → [].
Intuition Example: nums=[1,3,-1], k=3: Deque [1] (3 is max), output [3].
Implement
(See corrected code above.)

Review
Test cases: nums=[1,3,-1,-3,5,3,6,7], k=3 → [3,3,5,5,6,7], nums=[1], k=1 → [1], nums=[] → [].
Verify: Trace deque for nums=[1,3,-1], k=3: Deque holds index of 3, then -1.
Evaluate
Time: O(n) (each element pushed/popped at most once).
Space: O(k) for deque, O(n-k+1) for result.
Brute-Force: O(n * k).
Tie-In to Your Context
Sliding Window: Your Minimum Window Substring and Character Replacement questions used sliding windows. This problem aligns with your pattern (two inputs → sliding window).
Decision Tree: Per your clarification, I avoided forcing a tree. The brute-force (scanning windows) is linear, not recursive, unlike Word Break.
List Operations: You asked about append (O(1)). This code uses deque operations (O(1)) and list append (O(1)), aligning with your focus.
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0 or k > len(nums):
            return []
        res = []
        q = collections.deque()
        l, r = 0, 0
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:  # Remove smaller elements from deque's back
                q.pop()
            q.append(r)
            if l > q[0]:  # Remove out-of-window indices
                q.popleft()
            if r + 1 >= k:  # Window size is k
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res