class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr=[]
        for i in range(1,len(nums)+2):
            val=i*k
            if val not in nums:
                return val
        
        