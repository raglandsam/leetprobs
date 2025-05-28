class Solution(object):
    def isValid(self, s):
        if len(s)%2!=0 or len(s)==0:
            return False 
        else :
            r=[]
            d={")":"(","}":"{","]":"["}
            for c in s:
                if c in d:
                    if r and r[-1]==d[c]:
                        r.pop() 
                    else:
                        return False 
                else:
                    r.append(c)
        return not r


                        



        