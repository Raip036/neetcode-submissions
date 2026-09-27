class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dic_s = {}
        dic_t = {}

        for char in s:
            if char in dic_s:
                dic_s[char] += 1

            else:
                dic_s[char] = 1

        for char in t:
            if char in dic_t:
                dic_t[char] += 1

            else:
                dic_t[char] = 1

        return dic_s == dic_t