class Solution(object):
    def plusOne(self, digits):
        string = "".join(map(str, digits))
        number = int(string)

        number = number + 1

        digits = list(str(number))
        digits = list(map(int, digits))

        return digits