class Solution(object):
    def maxAlternatingSum(self, nums):
        nums = sorted(i * i for i in nums)
        i = 0
        j = len(nums) - 1 
        total = 0
        while i<j:
            total = total + (nums[j]- nums[i])
            i = i + 1
            j = j -1
        if i==j:
            total = total + nums[i]
        return total 
