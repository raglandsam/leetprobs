class Solution(object):
    def compress(self, chars):
        r=0
        w=0
        while r < len(chars):
            char= chars[r]
            c=0
            while r< len(chars) and chars[r]==char:
                r+=1
                c+=1
            chars[w]=char
            w+=1
            if c>1:
                for dig in str(c):
                    chars[w]=dig
                    w+=1
            
        return w

        