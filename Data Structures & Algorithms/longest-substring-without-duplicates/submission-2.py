class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        checker = set()
        left = 0
        counter = 0
        for right in range(len(s)):
            if s[right] not in checker:
                checker.add(s[right])
                counter = max(counter, right-left + 1)
            elif s[right] in checker:
                while s[right] in checker:
                    checker.remove(s[left])
                    left += 1
                checker.add(s[right])
                counter = max(counter, right-left + 1)
                
        
        return counter
        
      
            
            
            




        