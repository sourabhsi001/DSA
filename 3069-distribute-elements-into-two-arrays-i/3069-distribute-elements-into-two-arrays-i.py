class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=[]
        arr2=[]
        arr1.append(nums[0])
        arr2.append(nums[1])
        i=2
        while len(nums)>i:
            peak1=arr1[-1]
            peak2=arr2[-1]
            if peak1>peak2:
                arr1.append(nums[i])
                i+=1
            else:
                arr2.append(nums[i])
                i+=1
        result=[]
        for i in arr1:
            result.append(i)
        for i in arr2:
            result.append(i)
        return result

        
        