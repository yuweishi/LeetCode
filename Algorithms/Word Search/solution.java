public class Solution {
    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[0].length; j++){
                if (check(board, i, j, word, 0))
                    return true;
            }
        }
        return false;
    }
    public boolean check(char[][] board, int i, int j, String word, int pos){
        if (pos == word.length())
            return true;
        if (i < board.length && i >= 0 && j < board[0].length && j >= 0 && board[i][j] != '*' && board[i][j] == word.charAt(pos)){
            char cur = board[i][j];
            //visit.add((i, j))
            board[i][j] = '*';
            pos += 1;
            if (check(board, i, j + 1, word, pos))
                return true;
            if (check(board, i, j - 1, word, pos))
                return true;
            if (check(board, i + 1, j, word, pos))
                return true;
            if (check(board, i - 1, j, word, pos))
                return true;
            //visit.remove((i, j))
            board[i][j] = cur;
        }
        return false;
    }
}
