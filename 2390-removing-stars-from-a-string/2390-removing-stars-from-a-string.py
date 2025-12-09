class Solution(object):
    def removeStars(self, s):
        l=[]
        for i in s :
            if i.isalpha():
                l.append(i)
            elif i=="*":
                if l:
                    l.pop()
        return ''.join(l)

            
