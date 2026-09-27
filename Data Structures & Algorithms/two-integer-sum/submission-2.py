class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}

        for i, value in enumerate(nums):
            dic[value] = i

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in dic and dic[difference] != i:
                return [i, dic.get(difference)]