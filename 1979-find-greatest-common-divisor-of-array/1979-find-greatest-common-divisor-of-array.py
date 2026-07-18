class Solution:
    def findGCD(self, nums: List[int]) -> int:
        ans=math.gcd(max(nums),min(nums))
        return ans
        