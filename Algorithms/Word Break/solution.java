public class Solution {
    public boolean wordBreak(String s, Set<String> wordDict) {
        if (s == null || s.length() == 0) return true;
        ArrayList<Integer> dp = new ArrayList<>();
        dp.add(0);
        for (int i = 1; i < s.length() + 1; i++){
            for (int start: dp){
                if (wordDict.contains(s.substring(start, i))){
                    dp.add(i);
                    break;
                }
            }
        }
        return (dp.get(dp.size() - 1) == s.length());
    }
}
