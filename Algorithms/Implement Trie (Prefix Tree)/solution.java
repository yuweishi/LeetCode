class TrieNode {
    // Initialize your data structure here.
    public boolean isWord = false;
    public HashMap<Character, TrieNode> dict = new HashMap<Character, TrieNode>();
}

public class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        TrieNode current = root;
        for (Character c : word.toCharArray()) {
            if (!current.dict.containsKey(c))
                current.dict.put(c, new TrieNode());
            current = current.dict.get(c);
        }
        current.isWord = true;
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
        TrieNode current = root;
        for (Character c : word.toCharArray()) {
            if (!current.dict.containsKey(c))
                return false;
            current = current.dict.get(c);
        }
        return current.isWord;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
        TrieNode current = root;
        for (Character c : prefix.toCharArray()) {
            if (!current.dict.containsKey(c))
                return false;
            current = current.dict.get(c);
        }
        return true;
    }
}

// Your Trie object will be instantiated and called as such:
// Trie trie = new Trie();
// trie.insert("somestring");
// trie.search("key");
