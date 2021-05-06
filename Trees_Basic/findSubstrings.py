class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        current = self.root
        for el in word:
            if el not in current.children:
                current.children[el] = TrieNode()
            current = current.children[el]
        current.isEnd = True
    def search(self, word):
        current = self.root
        for el in word:
            if el in current.children:
                current = current.children[el]
            else:
                return False
        return current.isEnd
def findSubstrings(words, parts):
    trie = Trie()
    ans = []
    for part in parts: trie.insert(part)
    parts = sorted(set([len(part) for part in parts]), reverse = True)
    for index, word in enumerate(words):
        for length in parts:
            i = 0
            flag = False
            while i <= len(word) - length:
                curWord = word[i : i + length]
                if trie.search(curWord):
                    words[index] = word[:i] + '[' + curWord + ']' + word[i + length : len(word)]
                    flag = True
                    break
                i += 1
            if flag: break
    return words