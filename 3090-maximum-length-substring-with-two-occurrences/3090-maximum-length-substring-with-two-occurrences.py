class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans=0
        fre={}
        j=0
        for i in range(len(s)):
            fre[s[i]]=fre.get(s[i],0)+1

            while fre[s[i]]>2:
                fre[s[j]]-=1
                j+=1

            ans=max(ans,i-j+1)
        return ans





