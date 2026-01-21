class Solution(object):
    def isValid(self, s):
        d={")":"(","}":"{","]":"["}
        stac=[]
        if len(s)==1:
            return False 
        for i in s:
            if i in d:
                if stac and stac[-1]==d[i]:
                    stac.pop()
                else:
                    return False 
            else:
                stac.append(i)
                
        return True if not stac else False 
            