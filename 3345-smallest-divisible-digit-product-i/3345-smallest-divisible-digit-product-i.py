class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+11):
            num=str(i)
            multi=1
            for j in  num:
                multi*=int(j)
            
            if multi%t==0:
                return i
            else:
                multi=1



        