class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        while True:
            prod=i*i
            if prod==x:
                return i
            if prod > x:
                return i-1
            i+=1