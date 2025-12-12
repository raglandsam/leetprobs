class Solution(object):
    def asteroidCollision(self, asteroids):
        stack=[]
        for i in asteroids :
            aliveflag= True 
            while stack and ((i<0) and (stack[-1]>0)):
                if abs(i) > abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(i)==abs(stack[-1]):
                    stack.pop()
                aliveflag=False
                break
            if aliveflag:
                stack.append(i)

        return stack 

        