class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_ans=float("-inf")
        c_sum=0
        for i in range(len(nums)):
            if c_sum + nums[i]<nums[i]:
                c_sum=nums[i]
            else:
                c_sum+=nums[i]
            max_ans=max(max_ans,c_sum)
        return max_ans
            

        