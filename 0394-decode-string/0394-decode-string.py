class Solution(object):
    def decodeString(self, s):
        
        i=0
        def decode(i):
            num=0
            res=""          
            while i < len(s):
                if s[i].isdigit():
                    num=num*10+int(s[i])
                    i+=1
                elif s[i]=="[":
                    i+=1
                    decodestr,i=decode(i)
                    res+=decodestr*num
                    num=0
                elif s[i]=="]":
                    return res,i+1
                else:
                    res+=s[i]
                    i+=1
            return res , i
        decoded,_=decode(0)
        return decoded