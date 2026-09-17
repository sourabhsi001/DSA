class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # i=0
        # j=0
        # while i<len(nums1):
        #     if nums1[i]<=nums2[j]:

        #         i+=1
        #     elif nums1[i]>nums2[j]:
        #         nums2[j],nums1[i]=nums1[i],nums2[j]
        #         i+=1
        #         j+=1
        n=len(nums1)-1
        for i in range(len(nums2)):
            nums1[n]=nums2[i]
            n-=1
        return nums1.sort()

            
        


        
        