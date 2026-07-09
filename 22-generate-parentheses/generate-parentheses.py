class Solution(object):
    def generateParenthesis(self, n):
        result=[]
        pairs='()'
        def valid(c):
            d={'(':')'}
            s=[]
            if len(c)==1:
                return False
            for p in c:
                if p in d:
                    s.append(d[p])
                else:
                    if s and s[-1]==p:
                        s.pop()
                    else:
                        return False
            return True if not s else False
        def backtrack(path):
            if len(path)==2*n:
                if valid(path):
                    result.append(''.join(path))
                return
            for p in pairs:
                path.append(p)
                backtrack(path)
                path.pop()
        backtrack([])
        return result