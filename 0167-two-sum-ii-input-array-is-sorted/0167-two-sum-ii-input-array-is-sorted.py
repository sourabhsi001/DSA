class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans=[]
        i=0
        j=len(nums)-1
        while j>i:
            jod=nums[i]+nums[j]
            if jod > target:
                j-=1
            elif jod< target:
                i+=1
            elif jod == target:
                ans.append(i+1)
                ans.append(j+1)
                return ans
        
