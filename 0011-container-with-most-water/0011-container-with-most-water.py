class Solution(object):
    def maxArea(self, height):
        i=0
        j=len(height)-1
        max_wot=0
        while i<j:
            max_wot= max(max_wot,(j-i)*(min(height[i],height[j])))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_wot