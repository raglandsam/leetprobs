class Solution(object):
    def fib(self,n):
        f=[0,1]
        for i in range(1,n):
            f.append(f[-1]+f[-2])
        return f[n]
        