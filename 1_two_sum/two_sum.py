class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {} # value: index 
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dict:
                indexes = [dict[diff], i]
                return indexes 
            dict[n] = i