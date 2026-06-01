"""
Below is the **UMP** (Understand, Match, Plan) for the **Maximum Product Subarray** problem, tailored to be concise and aligned with the UMPIRE approach for interview preparation.

### Understand
- **Objective**: Find the contiguous subarray within a given integer array `nums` that has the maximum product, and return that product.
- **Clarifying Questions**:
  - Are integers positive, negative, or zero? (Assume all possible).
  - Are non-integers possible? (Assume integers only).
  - Array constraints? (Assume `1 ≤ len(nums) ≤ 2 * 10^4`, `-10^4 ≤ nums[i] ≤ 10^4`).
- **Test Cases**:
  - `[2, 3, -2, 4]` → `6` (subarray `[2, 3]`).
  - `[-2, 0, -1]` → `0` (zero or single elements).
  - `[-2]` → `-2` (single element).
- **Edge Cases**:
  - Single element (e.g., `[-2]`).
  - All negatives (e.g., `[-2, -3]` → `6`).
  - Zeros (e.g., `[-2, 0, -1]`).
  - Large numbers (within bounds).

### Match
- **Pattern**: Dynamic programming, similar to Kadane’s algorithm for maximum sum subarray, but tracks both maximum and minimum products due to negative numbers flipping signs.
- **Why DP**: Negatives and zeros make sliding window or greedy approaches infeasible (e.g., `[-2, -3]` → `6` requires keeping negative products).
- **Alternatives Ruled Out**:
  - Brute force: O(n²) checking all subarrays, too slow.
  - Sliding window: Fails due to sign changes and resets by zeros.

### Plan
- Initialize `maxProd`, `curMin`, `curMax` to `nums[0]` to handle the first element.
- For each `num` in `nums[1:]`:
  - Save `temp = curMax * num` to avoid overwriting `curMax`.
  - Update `curMax = max(num, temp, curMin * num)` (start new subarray or extend).
  - Update `curMin = min(num, temp, curMin * num)` (track negative products).
  - Update `maxProd = max(maxProd, curMax)` to track global max.
- Return `maxProd`.
- **Pseudocode**:
  ```
  if not nums: return 0
  maxProd = nums[0]
  curMin, curMax = nums[0], nums[0]
  for num in nums[1:]:
      temp = curMax * num
      curMax = max(num, temp, curMin * num)
      curMin = min(num, temp, curMin * num)
      maxProd = max(maxProd, curMax)
  return maxProd
  ```

This UMP is concise, covers the essentials, and sets up a correct implementation for the **Maximum Product Subarray** problem, addressing negatives and zeros without pointers by using DP to dynamically track products.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxProd = nums[0]
        curMin, curMax = 1, 1
        for num in nums:
            tmp = curMin
            curMin = min(num, num * curMin, num * curMax )
            curMax = max(num, num * tmp, num * curMax )
            maxProd = max(curMax, maxProd)
        return maxProd

        