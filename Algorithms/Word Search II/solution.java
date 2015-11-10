class TrieNode {
    // Initialize your data structure here.
    public boolean isWord = false;
    public HashMap<Character, TrieNode> dict = new HashMap<Character, TrieNode>();
}

class Trie {
    public TrieNode root = new TrieNode();

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
}

public class Solution {
    private HashSet<String> res = new HashSet<String>();
    public List<String> findWords(char[][] board, String[] words) {
        Trie trie = new Trie();
        for (String word: words)
            trie.insert(word);
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                check(board, trie.root, i, j, "");
            }
        }
        return new ArrayList<String>(res);
    }
    
    public void check(char[][] board, TrieNode trie, int i, int j, String pre) {
        if (i >= 0 && i < board.length && j >= 0 && j < board[0].length && board[i][j] != '*' && trie.dict.containsKey(board[i][j])) {
            pre += board[i][j];
            board[i][j] = '*';
            TrieNode subtrie = trie.dict.get(pre.charAt(pre.length() - 1));
            if (subtrie.isWord)
                res.add(pre);
            check(board, subtrie, i, j + 1, pre);
            check(board, subtrie, i, j - 1, pre);
            check(board, subtrie, i + 1, j, pre);
            check(board, subtrie, i - 1, j, pre);
            //visit.remove((i, j))
            board[i][j] = pre.charAt(pre.length() - 1);
        }
    }
}
