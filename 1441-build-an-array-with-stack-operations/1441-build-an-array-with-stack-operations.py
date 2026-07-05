class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operation=[]
        max_num=max(target)
        
        i=0
        for k in range(1,max_num+1):
             if k==target[i]:
                    operation.append("Push")
                    i+=1
                
             else:
                    operation.append("Push")
                    operation.append("Pop")   

        return operation


        

        