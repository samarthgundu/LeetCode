class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        rev = str(x)[::-1]
        rev = int(rev)
        return x == rev