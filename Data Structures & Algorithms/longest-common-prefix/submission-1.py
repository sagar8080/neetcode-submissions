class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = set()
        strs = sorted(strs)
        start = strs[0]
        end = strs[-1]
        prefix_len = 0
        for i in range(min(len(start), len(end))):
            if start[i] != end[i]:
                break
            prefix_len += 1
        return start[:prefix_len]