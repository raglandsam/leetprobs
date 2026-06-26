class Solution(object):
    def romanToInt(self, s):
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l=len(s)
        n=0
        for i in range(l):
            if i+1<l and d[s[i]] <d[s[i+1]]:
                n-=d[s[i]]
            else:
                n+=d[s[i]]
        return n     