from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      uniqueMap = {}
      for i in range(len(nums)):
        uniqueMap[nums[i]] = 0
      return list(uniqueMap.keys())
        
example = Solution()
print(example.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))      