class Solution(object):
    def isPowerOfThree(self, n):
        while (n>1):
            if n%3==0:
                n=n//3
            else :
                return False
        return n==1