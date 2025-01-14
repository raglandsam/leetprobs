class Solution(object):
    def search(self, arr,key ):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if key>arr[mid]:
                low=mid+1
            elif key<arr[mid] :
                high=mid-1
            elif arr[mid]==key:
                return mid
        return -1