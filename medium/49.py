class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            countS = [0] * 26
            for ch in s:
                countS[ord(ch) - ord('a')] += 1
            
            anagrams[tuple(countS)].append(s)

        return list(anagrams.values())











        
