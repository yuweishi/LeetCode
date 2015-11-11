public class Solution {
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
