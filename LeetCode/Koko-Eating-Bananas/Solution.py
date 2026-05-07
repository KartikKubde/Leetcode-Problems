1class Solution:
2
3    def guess_ka_ans(self,piles, n, speed):
4        h = 0
5        for i in range(n):
6            h = h + (piles[i])//speed 
7            if(piles[i]%speed != 0):
8                h+=1
9        return h
10
11    def minEatingSpeed(self, piles: List[int], h: int) -> int:
12        
13        n = len(piles)
14        low = 1
15        high = max(piles)
16        res = -1
17
18        while(low <= high):
19
20            guess = (low + high) // 2
21
22            hour = self.guess_ka_ans(piles,n,guess)
23
24            if(h < hour):
25                low = guess + 1
26            else:
27                res = guess
28                high = guess - 1
29
30        return res 