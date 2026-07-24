class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_gap=0
        if len(nums)<1:
            return 0
        for i in range(len(nums)-1):
            gap=nums[i+1]-nums[i]
            max_gap=max(gap,max_gap)
        
        if len(nums)==2:
            return nums[1]-nums[0]
            
        else:
            return max_gap
        