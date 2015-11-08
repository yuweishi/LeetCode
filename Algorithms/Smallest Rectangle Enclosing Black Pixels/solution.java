public class Solution {
    public int minArea(char[][] image, int x, int y) {
        int left = searchColumn(image, 0, y, true);
        int right = searchColumn(image, y + 1, image[0].length, false);
        int top = searchRow(image, 0, x, true);
        int bottom = searchRow(image, x + 1, image.length, false);
        return (right - left) * (bottom - top);
    }
    
    private int searchColumn(char[][] image, int start, int end, boolean opt) {
        while (start < end) {
            int mid = start + (end - start) / 2, i = 0;
            for (; i < image.length; i++) {
                if (image[i][mid] == '1')
                    break;
            }
            if (i < image.length == opt) 
                end = mid;
            else
                start = mid + 1;
        }
        return start;
    }
    
    private int searchRow(char[][] image, int start, int end, boolean opt) {
        while (start < end) {
            int mid = start + (end - start) / 2, i = 0;
            for (; i < image[0].length; i++) {
                if (image[mid][i] == '1') 
                    break;
            }
            if (i < image[0].length == opt) 
                end = mid;
            else
                start = mid + 1;
        }
        return start;
    }
}
