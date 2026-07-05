class Solution:

    def func(self,nums,n,idx,diary,ans):

        if(idx == n):
            ans.append(list(diary))
            return

        # Yes
        diary.append(nums[idx])
        self.func(nums,n,idx+1,diary,ans)
        diary.pop()

        #No
        self.func(nums,n,idx+1,diary,ans)

        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        idx = 0
        diary = []
        ans  = []

        self.func(nums,n,idx,diary,ans)
        return ans