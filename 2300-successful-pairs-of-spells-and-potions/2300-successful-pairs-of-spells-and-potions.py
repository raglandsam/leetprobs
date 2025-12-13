class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        
        arr=[]
        for i in range(len(spells)):
            idx=len(potions)
            l=0
            r=len(potions)-1
            while l<=r:
                mid=(l+r)//2
                if  potions[mid]*spells[i] >=success:
                    idx = mid
                    r=mid-1
                else:
                    l=mid+1
            arr.append(len(potions)-idx)
        return arr

            

        