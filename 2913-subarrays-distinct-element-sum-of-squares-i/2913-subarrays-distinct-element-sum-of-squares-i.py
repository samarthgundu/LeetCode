class Solution(object):
    def sumCounts(self, nums):
        count = 0
        for j in range(len(nums)):
            temp = []
            for i in range (j, len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                count = count+(len(temp)*len(temp))
        return count



        