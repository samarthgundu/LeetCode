class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""

        result = []

        while sum > 9:
            result.append('9')
            sum -= 9
            num -= 1

        if sum > 0:
            result.append(str(sum))
            num -= 1

        result.append('0' * num)

        return ''.join(result)