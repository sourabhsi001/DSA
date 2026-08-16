class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False

        count=False
        max_num=max(arr)
        if arr[0]==max_num:
            return False
        j=0
        for i in range(len(arr)-1):
    
            if arr[i]==max_num:
                j=i
                break
            if arr[i]>=arr[i+1]:
                return False
        
        for i in range(j,len(arr)-1):
            if arr[i]<=arr[i+1]:
                return False
               
        return True
        
        