class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n=len(nums1)-1
        for i in range(len(nums2)):
            nums1[n]=nums2[i]
            n-=1
        return nums1.sort()