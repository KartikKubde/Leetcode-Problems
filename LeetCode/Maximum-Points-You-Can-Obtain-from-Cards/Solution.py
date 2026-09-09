1class Solution(object):
2    def maxScore(self, cardPoints, k):
3        """
4        :type cardPoints: List[int]
5        :type k: int
6        :rtype: int
7        """
8        n = len(cardPoints)
9        if n == k:
10            return sum(cardPoints)
11
12        left_sum = 0
13        right_sum = 0 
14
15        for i in range(0,k):
16            left_sum += cardPoints[i]
17        
18        maxi = left_sum
19        right = n-1
20
21        for i in range(k-1,-1,-1):
22            left_sum -= cardPoints[i]
23            right_sum += cardPoints[right]
24            maxi = max(maxi,left_sum + right_sum)
25            right -= 1
26
27        return maxi
28