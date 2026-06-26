class Solution(object):
    def combine(self, n, k):
        result=[]

        def back_track(index,path):
            if len(path)==k :
                result.append(path[:])
                return
            for i in range(index,n+1):
                path.append(i)
                back_track(i+1,path)
                path.pop()
        back_track(1,[])
        return result
            


        