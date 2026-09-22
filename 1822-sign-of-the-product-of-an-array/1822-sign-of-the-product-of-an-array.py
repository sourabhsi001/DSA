class Solution:
    def arraySign(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i]>0:
                nums[i]=1
            elif nums[i]<0:
                nums[i]=-1
            else:
                nums[i]=0
        multi=1
        for i in nums:
            multi*=i
        return multi
