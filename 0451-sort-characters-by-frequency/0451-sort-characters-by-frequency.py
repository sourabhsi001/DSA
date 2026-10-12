class Solution:
    def frequencySort(self, s: str) -> str:
        fre={}
        for i in range(len(s)):
            fre[s[i]]=fre.get(s[i],0)+1
        sort_fre=sorted(fre.items(), key=lambda x: x[1], reverse=True)

        ans=""
        for i,j in sort_fre:
            ans+=i*j
        return ans
        
