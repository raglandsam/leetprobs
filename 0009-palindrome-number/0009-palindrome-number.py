class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False 
        n=x
        k=0
        while(n>0) :
            rem=n%10
            n//=10
            k=k*10+rem
        return True if k==x else False 

            