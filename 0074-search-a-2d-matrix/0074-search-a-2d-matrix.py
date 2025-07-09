class Solution(object):
    def searchMatrix(self, matrix, target):
        l=0
        rows=len(matrix)
        cols=len(matrix[0])
        r=rows*cols-1
        while(l<=r):
            mid=(l+r)//2
            row=mid//cols
            col=mid%cols
            if matrix[row][col]==target:
                return True
            elif target<matrix[row][col]:
                r=mid-1
            elif target>=matrix[row][col]:
                l=mid+1
               
        return False 
