class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort()
        # hashset = set()
        # prev = 0
        # current = 1
        # while current <= (len(nums)-1):
        #     if nums[current] - nums[prev] <= 1:
        #         hashset.add(nums[current])
        #         hashset.add(nums[prev])
        #         current +=1
        #         prev += 1
        #     else:
        #         break
        # return len(hashset)
            
        # nums = sorted(list(set(nums)))  # Remove duplicates, sort the list
        # longest = 0
        # current_longest = 1

        # for i in range(len(nums) - 1):
        #     if nums[i] + 1 == nums[i + 1]:
        #         current_longest += 1
        #     else:
        #         longest = max(longest, current_longest)
        #         current_longest = 1

        # longest = max(longest, current_longest)  # Update longest if necessary
        # return longest


        hashset = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in hashset: #No need to write the line about the else because no reasonable action will be taken for the else part other than to continue the iteration.
                currentlength = 1
                while (n+currentlength) in hashset:
                    currentlength += 1
                longest = max(longest, currentlength)
        return longest





        