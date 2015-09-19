public class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> res = new ArrayList<>();
        res.add(0);
        for (int i = 0; i < n; i++) {
            int j = res.size() - 1;
            while (j >= 0) {
                res.add((1 << i) + res.get(j));
                j--;
            }
        }
        return res;
    }
}
