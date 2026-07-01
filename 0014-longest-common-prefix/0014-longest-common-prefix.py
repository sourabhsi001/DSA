class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string=strs[0]
        for i in strs:
            result=os.path.commonprefix([string,i])
            string=result
        return string
            
                




        