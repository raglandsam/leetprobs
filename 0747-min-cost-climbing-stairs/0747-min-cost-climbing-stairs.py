class Solution(object):
    def minCostClimbingStairs(self, cost):
        if len(cost)<=2:
            if len(cost)==0:
                return 0
            else :
                return min(cost)
        else:
            dp=[0]*len(cost)
            dp[0]=cost[0]
            dp[1]=cost[1]
            for i in range(2,len(cost)):
                dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[-1] , dp[-2])

            
        

        