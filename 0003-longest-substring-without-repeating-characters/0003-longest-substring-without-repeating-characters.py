class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        subString = set()
        res = 0 
        
        for right in range(len(s)):
            while s[right] in subString:
                subString.remove(s[left])
                left += 1
            subString.add(s[right])
            res = max(res, right - left + 1)
        
        return res
