public class Solution {
    public void solveSudoku(char[][] board) {
        int[][] row = new int[9][9];
        int[][] col = new int[9][9];
        int[][] cube = new int[9][9];
        List<Integer> unknow = new ArrayList<Integer>();
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int num = board[i][j] - '1';
                    int k = i / 3 * 3 + j / 3;
                    row[i][num] = 1;
                    col[j][num] = 1;
                    cube[k][num] = 1;
                }
                else {
                    unknow.add(i * 9 + j);
                }
            }
        }
        helper(unknow, 0, row, col, cube, board);
    }
    
    public boolean helper(List<Integer> unknow, int index, int[][] row, int[][] col, int[][] cube, char[][] board) {
        if (index == unknow.size()) {
            return true;
        }
        int cur = unknow.get(index);
        int i = cur / 9;
        int j = cur % 9;
        int k = i / 3 * 3 + j / 3;
        for (int num = 0; num < 9; num++) {
            if (row[i][num] != 1 && col[j][num] != 1 && cube[k][num] != 1) {
                board[i][j] = (char) (num + '1');
                row[i][num] = 1;
                col[j][num] = 1;
                cube[k][num] = 1;
                if (helper(unknow, index + 1, row, col, cube, board)) {
                    return true;
                }
                board[i][j] = '.';
                row[i][num] = 0;
                col[j][num] = 0;
                cube[k][num] = 0;
            }
        }
        return false;
    }
}
