class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1

            else:
                dic[num] = 1

        result = []               

        for i in range(k):
            current = max(dic, key=dic.get)
            result.append(current)
            dic.pop(current)

        return result


       