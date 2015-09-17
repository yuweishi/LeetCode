public class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int area = (D - B) * (C - A) + (G - E) * (H - F);
        if (E >= C || A >= G || B >= H || F >= D){
            return area;
        }
        return area - (Math.min(C, G) - Math.max(A, E)) * (Math.min(D, H) - Math.max(B, F));
    }
}
