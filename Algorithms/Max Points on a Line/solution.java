/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
public class Solution {
    public int maxPoints(Point[] points) {
        int max = 0, same, submax;
        double x1, x2, y1, y2, key;
        HashMap<Double, Integer> dict;
        for (int i = 0; i < points.length; i++) {
            same = 1; x1 = points[i].x; y1 = points[i].y; submax = 0;
            dict = new HashMap<Double, Integer>();
            for (int j = i + 1; j < points.length; j++) {
                x2 = points[j].x; y2 = points[j].y;
                if (x1 == x2 && y1 == y2) {
                    same++;
                    continue;
                }
                if (x1 == x2) key = Double.POSITIVE_INFINITY;
                else if (y1 == y2) key = 0;
                else key = (y1- y2) / (x1 - x2);
                dict.put(key, dict.containsKey(key) ? dict.get(key) + 1 : 1);
                submax = Math.max(submax, dict.get(key));
            }
            max = Math.max(max, submax + same);
        }
        return max;
    }
}
