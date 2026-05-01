1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        
4        n = len(nums)
5        low = 0
6        high = n-1
7
8        while(low <= high):
9
10            guess = (high + low) // 2
11
12            if(nums[guess] > nums[n-1]):          # part 1
13
14                if(nums[guess] == target):
15                    return guess
16
17                elif(nums[guess] < target):
18                    low = guess + 1
19
20                else:
21                    if(nums[0] > target):
22                        low = guess + 1
23                    else:
24                        high = guess - 1
25
26            else:          # part 2
27
28                if(nums[guess] == target):
29                    return guess
30
31                elif(nums[guess] > target):
32                    high = guess -1
33
34                else:
35                    if(nums[n-1] < target):
36                        high = guess - 1
37                    else:
38                        low = guess + 1
39
40        return -1