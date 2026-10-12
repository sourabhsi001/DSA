class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        fre={}

        for i in strs:
            key=''.join(sorted(i))
            if key not in fre:
                fre[key]=[]
            fre[key].append(i)
        return list(fre.values())


