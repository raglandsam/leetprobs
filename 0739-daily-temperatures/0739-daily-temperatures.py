class Solution(object):
    def dailyTemperatures(self, temperatures):
        st=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while st and temperatures[st[-1]] < temperatures[i]:
                f=st.pop()
                ans[f]=i-f
            st.append(i)
        return ans
            
        