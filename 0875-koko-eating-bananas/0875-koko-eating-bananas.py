class Solution(object):
    def minEatingSpeed(self, piles, h):
        l=1
        r=max(piles)
        ans=r
        while l<=r:
            mid=l+(r-l)//2
            tot_hours=0
            for i in piles:
                tot_hours+=int(math.ceil(float(i)/mid))
            if tot_hours<=h:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
        


            