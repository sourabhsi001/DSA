from collections import deque

def to_binary(n):
     q=deque()
     
     q.append("1")
     
     for i in range(n):
         f=q.popleft()
         
         print(f)
         
         q.append(f+"0")
         q.append(f+"1")
print(to_binary(15))