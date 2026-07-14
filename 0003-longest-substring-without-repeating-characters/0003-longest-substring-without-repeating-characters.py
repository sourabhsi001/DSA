class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data={}
        substring=""
        for i in s:
            if i in substring:
                data[substring]=len(substring)
                
                while i in substring:
                    substring=substring[1:]
            substring+=i
        data[substring]=len(substring)
        ans=max(data.values())
        return ans
        
            
        


        