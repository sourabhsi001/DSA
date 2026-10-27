class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i=0
        j=len(nums)-1

        while j>=i:
            m=(i+j)//2
            if nums[m]<target:
                i=m+1
            elif nums[m]>target:
                j=m-1

            elif nums[m]==target:
                return m
        return i

