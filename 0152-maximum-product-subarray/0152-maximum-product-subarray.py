class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curr_min=nums[0]
        curr_max=nums[0]
        max_ans=nums[0]

        for i in range(1,len(nums)):
            x=nums[i]
            if x<0:
                curr_min,curr_max=curr_max,curr_min
            curr_min=min(curr_min*x,x)
            curr_max=max(curr_max*x,x)

            max_ans=max(max_ans,curr_max)
        return max_ans