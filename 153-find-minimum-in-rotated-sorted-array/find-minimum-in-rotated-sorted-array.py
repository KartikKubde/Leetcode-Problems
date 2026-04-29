class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        low = 0 
        high = n - 1
        res = -1

        while(low <= high):

            guess = (high + low) // 2

            if(nums[guess] > nums[n-1]):                # part2
                low = guess + 1
            
            else:                                         
                res = guess                         # part1
                high = guess - 1

        return nums[res]
        
        
        
        
        
        # wrong approach
        # n = len(nums)
        # low = 0 
        # high = n - 1
        # res = -1

        # while(low <= high):

        #     guess = (high + low) // 2

        #     if(guess < n-1 and nums[guess] < nums[guess+1]):
        #         low = guess + 1
            
        #     else:
        #         res = guess 
        #         high = guess - 1

        # return nums[res+1]