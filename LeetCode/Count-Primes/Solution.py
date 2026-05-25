1class Solution:
2    def countPrimes(self, n: int) -> int:
3        
4        if n <= 2:
5            return 0
6
7        cnt = 0
8        prime = [True]*(n+1)
9
10        prime[0] = False
11        prime[1] = False
12
13        for i in range(2,n):
14            if(prime[i]):
15                cnt += 1
16
17            for j in range(2*i,n,i):
18                prime[j] = False
19
20        return cnt