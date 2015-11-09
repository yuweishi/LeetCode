class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        root = self.root.dict
        for char in word:
            if char not in root:
                root[char] = {}
            root = root[char]
        root[None] = None

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root.dict
        for char in word:
            if char not in root:
                return False
            root = root[char]
        return None in root

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root.dict
        for char in prefix:
            if char not in root:
                return False
            root = root[char]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
