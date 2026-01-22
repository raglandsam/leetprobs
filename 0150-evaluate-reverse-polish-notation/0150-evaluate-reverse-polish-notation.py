class Solution(object):
    def evalRPN(self, tokens):
        res=0
        stack=[]
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else :
                r2=stack.pop()
                r1=stack.pop()
                if i=="+":
                    stack.append(r1+r2)
                elif i=="-":
                    stack.append(r1-r2)
                elif i=="*":
                    stack.append(r1*r2)
                else:
                    stack.append(int(float(r1)/r2))
        return stack[0]
                
        