class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        fre={}
        fre2={}
        for i in range(len(s)):
            a=s[i]
            b=t[i]

            if a in fre and fre[a]!=b:
                return False
            if b in fre2 and fre2[b]!=a:
                return False
            
            fre[a]=b
            fre2[b]=a
        return True
            