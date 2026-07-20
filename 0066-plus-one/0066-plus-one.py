class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        num=int("".join(map(str,digits)))
        num=num+1
        ans=list(map(int,str(num)))
        return ans
        