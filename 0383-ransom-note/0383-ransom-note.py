class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        fre={}
        for i in magazine :
            fre[i]=fre.get(i,0)+1
        
        for i in ransomNote :
            if i not in fre or fre[i]==0:
                return False
            fre[i]-=1
        return True
        