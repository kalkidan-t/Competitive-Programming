class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        i = 2 
        while i%2 != 0 or i%n != 0:
            i +=1
        return i        