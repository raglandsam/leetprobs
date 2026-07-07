class Solution(object):
    def findComplement(self, num):
        if num==0:
            return 1
        n=num
        r=''
        while n>0:
            r+=str(n%2)
            n//=2
        res=0
        for i in range(len(r)):
            if r[i]=='0':
                res+=1*(2**i)
            
        return int(res)


        
        




        