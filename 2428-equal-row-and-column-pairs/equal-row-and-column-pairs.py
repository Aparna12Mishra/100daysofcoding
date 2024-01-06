class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        a=0
        b=[]
        for i in range(len(grid)):
            c=[]
            for j in range(len(grid)):
                c.append(grid[j][i])
            b.append(c)
        d=0
        for i in range(len(grid)):
            for j in range(0,len(grid[i])):
                if(grid[i]==b[j]):
                    d+=1
        return d
        


                

        