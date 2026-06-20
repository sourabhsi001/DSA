#Find maximum element in every window of size 3.
arr = [1,3,-1,-3,5,3,6,7]
k=3
n=len(arr)
answer=[]
for i in range(0,n-k+1):
    winddow=arr[i:i+k]
    answer.append(max(winddow))
print(answer)    