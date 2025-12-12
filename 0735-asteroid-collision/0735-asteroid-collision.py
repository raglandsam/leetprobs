class Solution(object):
    def asteroidCollision(self, asteroids):
        stack=[]
        for i in asteroids :
            ITSALIVE = True
            while stack and ((i<0) and (0<stack[-1])):
                if abs(i) > abs(stack[-1]):
                    stack.pop()
                    continue
                if abs(i) ==abs(stack[-1]):
                    stack.pop()
                ITSALIVE= False
                break
            if ITSALIVE:
                stack.append(i)
        return stack
 

