class Solution(object):
    def reverse(self, x):
        sign = 1
        if x<0:
            sign =-1
        x=abs(x)
        n=0
        while x > 0:
            n=n*10+x%10
            x//=10
        if n<=math.pow(2,31)-1:
            if n> - math.pow(2,31):
                return sign*n
        
        return 0

        