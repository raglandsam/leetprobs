class Solution(object):
    def reverseWords(self, s):
        n=len(s)
        l=[]
        word =""
        for i in range(n):
            if s[i]!=" ":
                word+=s[i]
            else: 
                if word:
                    l.append(word)
                word=""
                continue
        if word :
            l.append(word)
        fw=""
        k=l[::-1]
        for i in range(len(k)):
            if i<len(k)-1:
                fw+=k[i]+" "
            else :
                fw+=k[i]
        return fw
                
                

        
             
