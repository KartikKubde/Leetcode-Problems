1class Solution(object):
2    def moveZeroes(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: None Do not return anything, modify nums in-place instead.
6        """
7        #gpt approach
8        n = len(nums)
9        i = 0 
10        j = 0 
11
12        for i in range(n):
13            if(nums[i] != 0):
14                nums[j] = nums[i]
15                j += 1
16
17        while(j < n):
18            nums[j] = 0
19            j += 1
20
21        return nums
22
23# my approach
24# n = len(nums)
25#         i = 0 
26#         j = n - 1
27
28#         while(i<j):
29#             while(nums[i] == 0):
30#                 nums[i],nums[j] = nums[j],nums[i]
31#                 j -= 1
32#             i += 1
33#         return nums