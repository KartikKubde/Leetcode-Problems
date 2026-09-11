1import heapq
2
3class Solution(object):
4    def findKthLargest(self, nums, k):
5        """
6        :type nums: List[int]
7        :type k: int
8        :rtype: int
9        """
10        ans = [] 
11        n = len(nums)
12
13        for i in range(k):
14            heapq.heappush(ans,nums[i])
15
16        for i in range(k,n):
17            if(nums[i] > ans[0]):
18                heapq.heappop(ans)
19                heapq.heappush(ans,nums[i])
20
21        return ans[0]