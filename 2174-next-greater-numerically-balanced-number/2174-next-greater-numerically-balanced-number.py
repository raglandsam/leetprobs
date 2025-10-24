class Solution(object):
    def nextBeautifulNumber(self, n):
        d=n+1
        while True:
            valid=True
            s=str(d)
            for ch in set(s):
                if s.count(ch)!=int(ch):
                    valid =False 
                    break
            if valid:
                return d  
            d+=1