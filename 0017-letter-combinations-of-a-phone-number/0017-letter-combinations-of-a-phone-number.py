class Solution(object):
    def letterCombinations(self, digits):
        d={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        n=len(digits)
        result = []
        def backtrack(index,path):
            if len(path)==n:
                result.append("".join(path))
                return
            for let in d[digits[index]]:
                path.append(let)
                backtrack(index+1,path)
                path.pop()
        backtrack(0,[])
        return result

