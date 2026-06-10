class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        n=len(candies)
        boo=[0]*n
        for i in range(n):
            if candies[i]+extraCandies >=max(candies):
                boo[i]=True
            else:
                boo[i]=False
        return boo
        