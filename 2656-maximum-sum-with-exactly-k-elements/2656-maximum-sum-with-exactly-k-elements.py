class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        high_num=max(nums)
        
        
        return (high_num*k)+(k-1)*((k-1)+1)//2


            

            
        


            
        