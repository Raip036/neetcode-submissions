class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        best = 0
        left = 0
        dic = {}

        for right in range(len(s)):
            dic[s[right]] = dic.get(s[right], 0) + 1
            

            while (right - left + 1) - max(dic.values()) > k:
                dic[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)

        return best
            

