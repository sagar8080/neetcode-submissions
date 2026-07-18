class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        res = ""

        for i in range(min(n1, n2)):
            res += word1[i] + word2[i]
        
        if n2 > n1:
            res += word2[n1:n2]
        else:
            res += word1[n2:n1]
        
        return res