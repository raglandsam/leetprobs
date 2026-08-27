class Solution(object):
    def countBits(self, n):
        ans=[0]*(n+1)
        for i in range(n+1):
            w=0
            k=i
            while k>0:
                k&=k-1
                w+=1
            ans[i]=w
        return ans
            