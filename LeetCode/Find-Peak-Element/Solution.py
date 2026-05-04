1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        
4        n = len(nums)
5        low = 0 
6        high = n-1
7
8        while(low < high):
9            guess = (high + low) // 2
10            
11            if(nums[guess] > nums[guess+1]):
12                high = guess
13            else:
14                low = guess + 1
15
16        return low
17        
18        
19        
20        
21        
22        
23        
24        
25        
26        
27        
28        
29        
30        
31        
32        # n = len(nums)
33        # low = 0
34        # high = n - 1
35
36        # if n == 1:
37        #     return 0
38
39        # while low <= high:
40
41        #     guess = (high + low) // 2
42
43        #     if guess > 0 and guess < n - 1:
44
45        #         if nums[guess - 1] < nums[guess] and nums[guess] > nums[guess + 1]:
46        #             return guess
47
48        #         elif nums[guess] < nums[guess - 1]:
49        #             high = guess - 1
50
51        #         else:
52        #             low = guess + 1
53
54        #     elif guess == 0:
55        #         if nums[0] > nums[1]:
56        #             return 0
57        #         else:
58        #             return 1
59
60        #     else:
61        #         if nums[n - 1] > nums[n - 2]:
62        #             return n - 1
63        #         else:
64        #             return n - 2
65