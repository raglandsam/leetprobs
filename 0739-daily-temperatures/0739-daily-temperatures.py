class Solution(object):
    def dailyTemperatures(self,T):
        n=len(T)
        o=[0]*n
        st=[]
        for i in range(n):
            while st and T[i] > T[st[-1]]:
                end=st.pop()
                o[end]=i-end
            st.append(i)    
        return o