class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fre={}
        for i in nums:
            fre[i]=fre.get(i,0)+1
        
        for i in fre:
            if fre[i]==1:
                return i

        