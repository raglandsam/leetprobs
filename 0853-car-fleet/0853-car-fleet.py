class Solution(object):
    def carFleet(self, target, position, speed):
        time =[float(target-p)/float(s) for p,s in zip(position,speed)]    
        cars=sorted(zip(position,time), key = lambda item : item[0] , reverse = True)
        stack=[cars[0]]
        for car in cars[1:] :
            leadfleet=stack[-1]
            if car[1] > leadfleet[1]:
                stack.append(car)
            else:
                continue
        return len(stack)



        