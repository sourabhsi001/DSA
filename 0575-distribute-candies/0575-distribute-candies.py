class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        arr={}
        for i in candyType:
            arr[i]=arr.get(i,0)+1
        
        capacity=len(candyType)//2
        if capacity<=len(arr):
            return capacity
        else:
            return len(arr)