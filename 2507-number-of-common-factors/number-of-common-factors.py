class Solution(object):
    def commonFactors(self, a, b):
        c=0
        lim=min(a,b)
        for i in range(1,lim+1):    
            if a%i==0 and b%i==0:
                c+=1
        return c    
        