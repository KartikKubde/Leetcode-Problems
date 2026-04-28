1class Solution:
2    def peakIndexInMountainArray(self, arr: List[int]) -> int:
3        
4        low = 0 
5        high = len(arr) - 1
6        res = -1
7
8        while(low <= high):
9            guess = (high + low) // 2
10
11            if(arr[guess] < arr[guess+1]):
12                low = guess + 1
13
14            else:
15                res = guess
16                high = guess - 1
17
18        return res