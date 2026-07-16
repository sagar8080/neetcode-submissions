from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            keys[key].append(word)
        return list(keys.values())