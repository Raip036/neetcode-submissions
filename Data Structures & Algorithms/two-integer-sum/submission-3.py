class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, value in enumerate(nums):
            difference = target - value
            if difference in seen:
                return [seen[difference], i]
            seen[value] = i
        
        