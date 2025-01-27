from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_water = 0
        
        while left != right:
            min_height = min(height[left], height[right])
            length = right - left

            max_water = max(min_height * length, max_water) 
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_water
    
example = Solution()    
print(example.maxArea([1,8,6,2,5,4,8,3,7]))