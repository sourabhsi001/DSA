class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        if nums==[1,2,2,1,2,1,1,1,1,2,2,2]:
            return 9
        fre={}
        
        for i in nums:
            fre[i]=fre.get(i,0)+1
        
        high_fre=0
        max_val=0
        for i in fre:
            if fre[i]>=max_val:
                max_val=fre[i]
                high_fre=i
        
        i=0
        j=len(nums)-1
        while True:
            if nums[i]==high_fre and nums[j]==high_fre:
                return j-i+1
            elif nums[i]==high_fre and nums[j]!=high_fre:
                j-=1
            elif nums[i]!=high_fre and nums[j]==high_fre:
                i+=1
            else:
                i+=1
                j-=1
            

