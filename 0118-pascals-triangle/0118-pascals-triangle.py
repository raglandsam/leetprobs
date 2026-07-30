class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row=[1]
        out=[row]
        for i in range(numRows-1):
            row=[1] + [row[j] + row[j+1] for j in range(len(row)-1)] +[1]
            out.append(row)
        return out