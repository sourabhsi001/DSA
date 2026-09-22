class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        ans=0
        print(citations)
        for i in range(len(citations)):
            if citations[i]>=i+1:
                ans+=1
        return ans
            

