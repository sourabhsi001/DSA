class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)-1<1:
            return nums[0]
        for i in range(0,len(nums)-1,2):
            if nums[i]!=nums[i+1]:
                return nums[i]

        return nums[len(nums)-1]