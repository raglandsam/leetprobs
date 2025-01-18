class Solution(object):
    def coinChange(self, coins, amount):
        coins.sort()
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for i in coins:
            for j in range(i,amount+1):
                dp[j]= min(dp[j],dp[j-i]+1)
        if dp[amount]!=float('inf'):
            return dp[amount]
        else:
            return -1
