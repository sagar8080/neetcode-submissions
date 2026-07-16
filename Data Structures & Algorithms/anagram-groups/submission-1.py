from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [""]
        groups = defaultdict(list)
        result = []
        for string in strs:
            base = ''.join(sorted(string))
            groups[base].append(string)
        
        for k, v in groups.items():
            result.append(v)
        
        return result

