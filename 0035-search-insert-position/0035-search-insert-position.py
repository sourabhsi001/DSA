class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
        else:
            for j in range(len(nums)):
                if nums[j]>target:
                    return j
            return len(nums)
                
        