class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        fre={}
        for f in nums:
            fre[f]=fre.get(f,0)+1
        high=0
        for i in fre.values():
            if i>high:
                high=i
        
        for key,val in fre.items():
            if val==high:
                return key

        