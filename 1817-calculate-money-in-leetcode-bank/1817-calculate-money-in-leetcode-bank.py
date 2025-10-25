class Solution(object):
    def totalMoney(self, n):
        k=n//7
        p=n%7
        tot=0
        adder=1
        while (k>0):
            for i in range(7):
                tot+=(adder+i)
            k-=1
            adder+=1
        for i in range(p):
            tot+=(adder)+i
        return tot


        