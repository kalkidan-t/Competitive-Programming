class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_string = ''.join(char.lower() for char in s if char.isalnum())
        
        left = 0
        right = len(final_string) - 1
          
        while left < right:
            if final_string[left] != final_string[right]:
                return False
            left += 1
            right -= 1
        return True
        