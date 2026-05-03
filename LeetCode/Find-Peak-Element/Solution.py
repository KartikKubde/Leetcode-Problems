1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        n = len(nums)
4        low = 0
5        high = n - 1
6
7        if n == 1:
8            return 0
9
10        while low <= high:
11
12            guess = (high + low) // 2
13
14            if guess > 0 and guess < n - 1:
15
16                if nums[guess - 1] < nums[guess] and nums[guess] > nums[guess + 1]:
17                    return guess
18
19                elif nums[guess] < nums[guess - 1]:
20                    high = guess - 1
21
22                else:
23                    low = guess + 1
24
25            elif guess == 0:
26                if nums[0] > nums[1]:
27                    return 0
28                else:
29                    return 1
30
31            else:
32                if nums[n - 1] > nums[n - 2]:
33                    return n - 1
34                else:
35                    return n - 2
36