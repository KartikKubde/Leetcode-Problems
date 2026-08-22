1class Solution(object):
2    def climbStairs(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        
8        memo = {1:1,2:2}
9
10        def func(n):
11            if n in memo:
12                return memo[n]
13            else:
14                memo[n] = func(n-1) + func(n-2)
15                return memo[n]
16
17        return func(n)