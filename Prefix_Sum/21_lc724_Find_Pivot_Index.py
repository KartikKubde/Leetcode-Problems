class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        sum = 0
        n = len(nums)

        for i in range(n):
            sum += nums[i]

        if(left == (sum - nums[0])):
            return 0

        for i in range(1,n):
            left += nums[i-1]
            right = sum - nums[i] - left
            if(left == right):
                return i
        
        return -1
