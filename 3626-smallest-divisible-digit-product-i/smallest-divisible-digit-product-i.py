class Solution(object):
    def smallestNumber(self, n, t):
        def prod(k):
            j=1
            while k > 0:
                l=k%10
                j*=l
                k//=10
            return j
        while True:
            if prod(n)%t==0:
                return n
            else:
                n+=1
        
