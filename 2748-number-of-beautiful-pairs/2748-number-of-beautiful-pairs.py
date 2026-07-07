class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            for j in range(i+1,n):
                first=nums[i]
                while first>=10:
                    first//=10
                last=nums[j]%10
                if gcd(first,last)==1:
                    count+=1
        return count