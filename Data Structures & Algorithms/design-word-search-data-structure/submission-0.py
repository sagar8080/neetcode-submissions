class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True
        

    def search(self, word: str) -> bool:
        n = len(word)

        def dfs(idx, root):
            node = root

            for i in range(idx, n):
                ch = word[i]

                if ch == '.':
                    for child in node.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if ch not in node.children:
                        return False
                    node = node.children[ch]
            return node.end_of_word
        
        return dfs(0, self.root)
        
