class Solution(object):
    def lengthOfLongestSubstring(self, s):
        result = 0

        for i in range(len(s)):
            list1 = []

            for j in range(i, len(s)):
                if s[j] in list1:
                    break
                else:
                    list1.append(s[j])

            result = max(result, len(list1))

        return result