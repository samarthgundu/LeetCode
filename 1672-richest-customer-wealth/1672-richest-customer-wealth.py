class Solution(object):
    def maximumWealth(self, accounts):
        wealth = []
        for i in range(len(accounts)):
            wealth.append(sum(accounts[i]))
        return max(wealth)
        