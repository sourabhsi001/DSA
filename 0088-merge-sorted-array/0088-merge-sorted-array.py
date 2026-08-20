class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=len(nums1)-1
        for i in nums2:
            nums1[j]=i
            j-=1
            

            
            
        return nums1.sort()


            



        