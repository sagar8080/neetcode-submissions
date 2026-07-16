class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}

        def compare(word):
            return [order_map[c] for c in word]
        
        return words == sorted(words, key=compare)