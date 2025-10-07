class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        k=len(flowerbed)
        i=0
        while (i<k):
            if flowerbed[i]==0:
                emp_l=(i==0) or (flowerbed[i-1]==0)
                emp_r=(i==k-1) or (flowerbed[i+1]==0)
                if emp_l and emp_r:
                    flowerbed[i]=1
                    n-=1
            i+=1
        return True if n<=0 else False 
        