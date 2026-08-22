class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n=str(n)
        s=0
        m=1
        for i in n:
            i=int(i)
            s+=i
            m*=i
        n=int(n)
        t=s+m
        
        if n%t==0:
            return True
        else:
            return False
