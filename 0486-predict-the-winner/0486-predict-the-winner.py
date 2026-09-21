class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        def recurse(left, right, p1, p2, p1_turn):
            if left > right :
                return p1>=p2
            if p1_turn:
                take_l=recurse(left+1,right,p1+nums[left],p2,False)
                take_r=recurse(left, right-1,p1+nums[right],p2,False)
                return take_l or take_r
            elif not p1_turn:
                take_l=recurse(left+1,right, p1,p2+nums[left],True)
                take_r=recurse(left,right-1, p1, p2+nums[right], True)
                return take_l and take_r
        return recurse(0,len(nums)-1,0,0,True)