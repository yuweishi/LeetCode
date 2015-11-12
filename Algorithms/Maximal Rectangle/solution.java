public class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0) 
            return 0;
        int max = 0;
        int[] dp = new int[matrix[0].length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == '1')
                    dp[j]++;
                else
                    dp[j] = 0;
            }
            max = Math.max(max, largestRectangleArea(dp));
        }
        return max;
    }
    
    public int largestRectangleArea(int[] height) {
        int res = 0, h = 0, len = 0;
        Stack<Integer> stack = new Stack<>();
        height = Arrays.copyOf(height, height.length + 1);
        height[height.length - 1] = 0;
        for (int i = 0; i < height.length; i++) {
            while (!stack.empty() && height[stack.peek()] > height[i]) {
                h = height[stack.pop()];
                len = stack.empty() ? i: (i - stack.peek() - 1);
                res = Math.max(res, len * h);
            }
            stack.push(i);
        }
        return res;
    }
}
