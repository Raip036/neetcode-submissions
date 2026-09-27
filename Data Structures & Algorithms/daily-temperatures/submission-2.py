class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = len(temperatures) * [0]
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_index, stack_temp = stack.pop()
                result[stack_index] = i - stack_index
            stack.append([i, temp])

        return result