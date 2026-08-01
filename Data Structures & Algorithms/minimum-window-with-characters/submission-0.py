from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT = Counter(t)

        l = 0
        have, need = 0, len(countT)
        res = [-1, -1]
        res_len = float("inf")
        window = defaultdict(int)

        for r in range(len(s)):
            cr = s[r]
            window[cr] += 1

            if cr in countT and window[cr] == countT[cr]:
                have += 1
            
            while have == need:
                cur_len = r - l + 1
                if cur_len < res_len:
                    res_len = cur_len
                    res = [l, r]
                
                cl = s[l]
                window[cl] -= 1
                
                if cl in countT and window[cl] < countT[cl]:
                    have -= 1
                
                l += 1
        
        l, r = res

        return s[l: r+1] if res_len != float("inf") else ""