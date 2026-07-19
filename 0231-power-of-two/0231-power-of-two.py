class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0 or n<0:
                return False
       
       
        for i in range(n):
            
            
            if 2**i==n:
                return True
            elif 2**i>n:
                return False
            
            
        
     
        