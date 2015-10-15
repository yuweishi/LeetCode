public class Solution {
    public List<String> generatePossibleNextMoves(String s) {
        int n = s.length(), i = 0;
        ArrayList<String> res = new ArrayList<String>();
        while (i < n - 1){
            if (s.charAt(i) == '+'){
                while (i + 1 < n && s.charAt(i + 1) == '+'){
                    res.add(s.substring(0, i) + "--" + s.substring(i + 2));
                    i++;
                }
            }
            i++;
        }
        return res;
    }
}
