class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      
        i=0
        j=len(nums)-1
        while j>i:
            jod=nums[i]+nums[j]
            if jod > target:
                j-=1
            elif jod< target:
                i+=1
            elif jod == target:
               
                return [i+1,j+1]
        
