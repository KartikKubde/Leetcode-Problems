class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        if n == 1:
            return 0

        while low <= high:

            guess = (high + low) // 2

            if guess > 0 and guess < n - 1:

                if nums[guess - 1] < nums[guess] and nums[guess] > nums[guess + 1]:
                    return guess

                elif nums[guess] < nums[guess - 1]:
                    high = guess - 1

                else:
                    low = guess + 1

            elif guess == 0:
                if nums[0] > nums[1]:
                    return 0
                else:
                    return 1

            else:
                if nums[n - 1] > nums[n - 2]:
                    return n - 1
                else:
                    return n - 2
