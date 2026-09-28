class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counts = {}
        left = 0
        max_freq = 0
        longest = 0

        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            max_freq = max(max_freq, counts[char])

            window = right - left + 1
            replacements = window - max_freq

            while replacements > k:
                counts[s[left]] -= 1
                left += 1
                window = right - left + 1
                replacements = window - max_freq

            longest = max(longest, right-left + 1)

        return longest
        
   
            

