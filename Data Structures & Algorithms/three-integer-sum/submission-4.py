class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = set()
       

        for i in range (len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                   

                elif total > 0:
                    k -= 1

                elif total < 0:
                    j += 1

        return [list(t) for t in result]
            

            