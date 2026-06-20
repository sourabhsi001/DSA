#max sum od subarray
arr = [2,1,5,1,3,2]
n=len(arr)
k=3
max_sum=0
max_subarray=[]
for i in range(0,n-k+1):
    window=arr[i:i+k]
    current_sum=sum(window)
    if current_sum>max_sum:
        max_sum=current_sum
        max_subarray=window

print(max_subarray)
