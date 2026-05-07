class Solution:

    def guess_ka_ans(self,piles, n, speed):
        h = 0
        for i in range(n):
            h = h + (piles[i])//speed 
            if(piles[i]%speed != 0):
                h+=1
        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        n = len(piles)
        low = 1
        high = max(piles)
        res = -1

        while(low <= high):

            guess = (low + high) // 2

            hour = self.guess_ka_ans(piles,n,guess)

            if(h < hour):
                low = guess + 1
            else:
                res = guess
                high = guess - 1

        return res 