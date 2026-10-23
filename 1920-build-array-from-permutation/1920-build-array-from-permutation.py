class Solution(object):
    def buildArray(self, nums):
        final = []

        for i in range(len(nums)):
            final.append(nums[nums[i]])
        return final