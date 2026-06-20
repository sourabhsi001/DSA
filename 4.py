#impliment binary serach
def find_by_binary(arr,target):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<target:
            low=mid
        elif arr[mid]==target:
            print("found")
            break
            
        else:
            high=mid
arr = [1,3,5,7,9]

target = 7

find_by_binary(arr,target)
        