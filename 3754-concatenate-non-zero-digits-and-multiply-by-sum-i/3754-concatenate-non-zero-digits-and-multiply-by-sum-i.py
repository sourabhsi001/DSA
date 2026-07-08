class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        num=n
        s=str(n)
        size=len(s)
        s=s.replace("0","")
        n=int(s)
        Sum=0
        for i in range(size):
            Sum+= num%10
            num=num//10
        
        return n*Sum
            
     