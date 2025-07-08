class Solution(object):
    def makeFancyString(self, s):
        p=s[0]
        count=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                count=1

            if count<=2:
                p+=s[i]
        return p

