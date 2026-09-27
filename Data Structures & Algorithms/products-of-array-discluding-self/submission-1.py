class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Store the product of all elements to the left of each index.
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Multiply by the product of all elements to the right.
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output



