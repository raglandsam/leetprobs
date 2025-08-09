class Solution(object):
    def myAtoi(self, s):
        sign = 1
        s=s.strip()
        if not s:
            return 0

        pow231= -(2**31)
        powplus231= 2**31-1
        num =0
        st=0
        if s[0]=="-":
            sign = -1
            st=1
         
        elif s[0]=="+":
            st=1  

        for i in range(st,len(s)):
            if s[i].isdigit() :
                num=num*10 + int(s[i])
            else:
                break
        num = num *sign
        if num < pow231 :
            return pow231
        elif num > powplus231:
            return powplus231
        else:
            return num 

        




        
