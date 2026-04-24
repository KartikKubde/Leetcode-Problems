1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        low = 0
4        high = len(nums) - 1
5
6        while(low <= high):
7
8            guess = (low + high) // 2
9
10            if(nums[guess] == target):
11                return guess
12
13            elif(nums[guess] < target):
14                low = guess + 1
15
16            else:
17                high = guess - 1
18
19        return -1
20            