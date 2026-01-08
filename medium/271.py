from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        single_str = ""

        for s in strs:
            single_str += str(len(s)) + "#" + s

        return single_str


    def decode(self, s: str) -> List[str]:
        res = []
        l = 0

        while l < len(s):
            r = l
            
            # achar o delimitador
            while s[r] != "#":
                r += 1

            lenght = int(s[l:r])

            start = r + 1
            end = start + lenght
            res.append(s[start:end])

            l = end

        return res
