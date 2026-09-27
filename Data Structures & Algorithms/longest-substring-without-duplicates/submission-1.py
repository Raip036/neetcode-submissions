class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        checker = set()

        best = 0 
        left = 0
        right = 0

        for right in range(len(s)):
            while s[right] in checker:
                checker.remove(s[left])
                left += 1
            checker.add(s[right])
            best = max(best, right - left + 1)

        return best
            
            
            




        