class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        int_num = 0
        
        for i in range(len(s)):
            if i < len(s)-1 and  roman_num[s[i]] < roman_num[s[i+1]]:
                int_num -= roman_num[s[i]]
            else:
                int_num += roman_num[s[i]]
        return int_num
        