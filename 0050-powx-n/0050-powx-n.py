class Solution(object):
    def myPow(self, x, n):
        if n==0:
            return 1.0
        res=1.0
        if n < 0:
            n=-n
            x=float(1/x)
        curr_prod=x
        while n>0:
            if n%2==1:
                res*=curr_prod
            curr_prod= curr_prod*curr_prod
            n//=2
        return res


