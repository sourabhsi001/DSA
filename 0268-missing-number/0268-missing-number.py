class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            n=len(nums)
            if i+1 not in nums:
                return i+1
        return 0
                
            
        