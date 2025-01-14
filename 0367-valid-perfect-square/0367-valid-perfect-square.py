class Solution(object):
    def isPerfectSquare(self, num):
        if num<0 or num==0 :
            return False
        else :
            p=num**(0.5)
            if p%1==0:
                return True
            else:
                return False 