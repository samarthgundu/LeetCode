class Solution(object):
    def containsDuplicate(self, nums):
        s = set(nums)
        l = len(nums)
        if len(s) == l:
            return False
        else:
            return True
