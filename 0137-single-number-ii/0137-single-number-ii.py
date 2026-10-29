class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        fre={}
        for i in range(len(nums)):
            fre[nums[i]]=fre.get(nums[i],0)+1
        for i in fre:
            if fre[i]==1:
                return i