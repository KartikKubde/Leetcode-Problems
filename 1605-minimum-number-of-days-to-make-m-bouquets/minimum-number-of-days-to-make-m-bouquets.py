class Solution:

    def canMakeMBouq(self, bloomDay, guess, k):
        n = len(bloomDay)
        count = 0
        bouq_count = 0

        for i in range(n):

            if(bloomDay[i] <= guess):
                count += 1 
            else:
                count = 0 

            if(count == k):
                bouq_count += 1
                count = 0

        return bouq_count

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low = 0 
        high = max(bloomDay)
        minDays = -1

        while(low <= high):

            guess = (low + high) // 2

            bouq_count = self.canMakeMBouq(bloomDay, guess, k)

            if(bouq_count < m):
                low = guess + 1
            else:
                minDays = guess
                high = guess - 1 

        return minDays