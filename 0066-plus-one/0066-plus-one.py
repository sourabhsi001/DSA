class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        nums=int("".join(map(str,digits)))
        num=nums+1
        ans= list(map(int,str(num)))
        return ans
        

