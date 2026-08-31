class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        largest = 0

        for h in range(len(heights)):
            while l < r:
                width = r - l
                height = 0
                if heights[l] > heights [r]:
                    height = heights[r]
                    r -= 1
                else:
                    height = heights[l]
                    l += 1
                area = width * height
                largest = max(largest, area)

        return largest
                

