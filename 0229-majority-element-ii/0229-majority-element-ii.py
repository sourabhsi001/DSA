class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        box={}
        for i in nums:
            box[i]=box.get(i,0)+1
        ans=[]
        k=0
        limit=len(nums)//3
        for i,j in box.items():
            if j>limit:
                ans.append(i)
        return ans
            
            
            
            

             
        