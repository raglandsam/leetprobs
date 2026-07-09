class Solution(object):
    def isSameAfterReversals(self, num):
        if num==0:
            return True
        x=num
        res1=0
        while num>0:
            res1=res1*10 + num%10
            num//=10
        res2=0
        while res1>0:
            res2=res2*10 + res1%10
            res1//=10
        return x==res2
        
        