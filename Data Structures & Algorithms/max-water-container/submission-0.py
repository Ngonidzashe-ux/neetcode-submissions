class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # behind = 0
        # ahead = 1
        # maxarea = 0
        # while ahead <= (len(heights) - 1):
        #     area = min(heights[behind], heights[ahead]) * (ahead - behind)
        #     maxarea = max(area, maxarea)
        #     ahead += 1
        #     if ahead <= (len(heights) - 1) and heights[ahead] > heights[behind]:
        #         behind += 1

        # return maxarea

        l, r = 0, (len(heights) - 1)
        maxarea = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxarea = max(area, maxarea)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return maxarea


        