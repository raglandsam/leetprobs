class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        n=len(candies)
        boo=[0]*n
        p=max(candies)
        for i in range(n):
            if candies[i]+extraCandies >=p:
                boo[i]=True
            else:
                boo[i]=False
        return boo
        