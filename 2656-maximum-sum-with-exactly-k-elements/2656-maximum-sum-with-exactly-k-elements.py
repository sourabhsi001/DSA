class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        high_num=max(nums)
        ans=0
        for i in range(k):
            ans=ans+(high_num)
            high_num+=1
        
        return ans


            

            
        


            
        