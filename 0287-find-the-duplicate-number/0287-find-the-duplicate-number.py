class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        box={}
        for i in nums:
            box[i]=box.get(i,0)+1
        for i,j in box.items():
            if j>1:
                return i
        