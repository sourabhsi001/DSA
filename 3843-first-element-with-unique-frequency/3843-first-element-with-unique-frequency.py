class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        fre={}
        fre_count={}
        uniqe_list=list(set(nums))
        
        

        for num in nums:
          fre[num] = fre.get(num, 0) + 1
        
        for f in fre.values():
            fre_count[f]=fre_count.get(f,0)+1

        for num in nums:
            if fre_count[fre[num]] == 1:
               return num

        return -1
        




