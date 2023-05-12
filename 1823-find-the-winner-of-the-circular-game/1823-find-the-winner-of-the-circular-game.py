class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i+1 for i in range(n)]  
        next_friend = 0  
        while len(arr) > 1: 
            next_friend = (next_friend + k - 1) % len(arr)  
            arr.pop(next_friend)  
        return arr[0]
