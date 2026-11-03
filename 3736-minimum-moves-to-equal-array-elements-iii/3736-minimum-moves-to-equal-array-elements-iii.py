class Solution(object):
    def minMoves(self, nums):
        max_num = max(nums)
        result = 0
        diff = 0
        for i in nums:
            if i == max_num:
                continue
            else:
                diff=max_num-i
                result = result + diff
        return result
            

        