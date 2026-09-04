class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        min_arr=[0]*n
        min_arr[n-1]=nums[n-1]\

        for i in range(n-2,-1,-1):
            min_arr[i]=min(min_arr[i+1],nums[i])
        
        left_max=nums[0]

        for i in range(n):
            left_max=max(left_max,nums[i])

            if left_max-min_arr[i]<=k:
                return i
        return -1