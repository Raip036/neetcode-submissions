class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        best = 0
        left = 0
        right = len(heights) - 1
        
        while left < right:

            if heights[left] < heights[right]:
                area = heights[left] * (right - left)
                left += 1
            
            elif heights[left] > heights[right]:
                area = heights[right] * (right - left)
                right -= 1

            else:
                area = heights[right] * (right - left)
                right -= 1

            if area > best:
                best = area

        return best