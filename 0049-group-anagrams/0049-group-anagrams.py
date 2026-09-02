class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        fre={}

        for i in strs:
            key=''.join(sorted(i))
            if key not in fre:
                fre[key]=[]
            fre[key].append(i)
        return list(fre.values())
