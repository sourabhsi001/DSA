class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_table = {}
        t_table = {}

        for ch in s:
            s_table[ch] = s_table.get(ch, 0) + 1

        for ch in t:
            t_table[ch] = t_table.get(ch, 0) + 1

        for ch in t:
            if ch not in s_table or s_table[ch] != t_table[ch]:
                return ch