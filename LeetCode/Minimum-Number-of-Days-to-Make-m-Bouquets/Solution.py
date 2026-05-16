1class Solution:
2
3    def canMakeMBouq(self, bloomDay, guess, k):
4        n = len(bloomDay)
5        count = 0
6        bouq_count = 0
7
8        for i in range(n):
9
10            if(bloomDay[i] <= guess):
11                count += 1 
12            else:
13                count = 0 
14
15            if(count == k):
16                bouq_count += 1
17                count = 0
18
19        return bouq_count
20
21    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
22        low = 0 
23        high = max(bloomDay)
24        minDays = -1
25
26        while(low <= high):
27
28            guess = (low + high) // 2
29
30            bouq_count = self.canMakeMBouq(bloomDay, guess, k)
31
32            if(bouq_count < m):
33                low = guess + 1
34            else:
35                minDays = guess
36                high = guess - 1 
37
38        return minDays