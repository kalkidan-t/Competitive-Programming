class Solution: 
    def select(self, arr, i):
        # code here 
        minindex = i
        for i in range(i, len(arr) - 1):
            for j in range(i+1, len(arr)):
                if arr[j] < arr[minindex]:
                    minindex = j
        return minindex
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            minindex = self.select(arr, i)
            if arr[minindex] < arr[i]:
                arr[i], arr[minindex] = arr[minindex], arr[i]
