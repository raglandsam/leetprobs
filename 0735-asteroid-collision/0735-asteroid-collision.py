class Solution(object):
    def asteroidCollision(self, asteroids):
        stack=[]
        for i in asteroids :
            rightsmall = True
            while stack and ((i<0) and (0<stack[-1])):
                if abs(i) > abs(stack[-1]):
                    stack.pop()
                    continue
                if abs(i) ==abs(stack[-1]):
                    stack.pop()
                rightsmall= False
                break
            if rightsmall:
                stack.append(i)
        return stack
 

