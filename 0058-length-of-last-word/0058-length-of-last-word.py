class Solution(object):
    def lengthOfLastWord(self, s):
        result = s.split()
        i=len(result)-1
        return len(result[i])
        