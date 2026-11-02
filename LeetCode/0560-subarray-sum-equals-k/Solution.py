class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        n = len(nums)
        res = 0

        for i in range(n):
            sum += nums[i]
            ques = sum - k
            f = hashmap[ques]
            res += f
            hashmap[sum] += 1

        return res
