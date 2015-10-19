public class Solution {
    HashMap<String, List<String>> map = new HashMap<>();
    ArrayList<Integer> dp = new ArrayList<>(); 
    public List<String> wordBreak(String s, Set<String> wordDict) {
        List<String> ans = new ArrayList<>();
        if (s == null || s.length() == 0) return ans;
        dp.add(0);
        for (int i = 1; i < s.length() + 1; i++){
            for (int start: dp){
                if (wordDict.contains(s.substring(start, i))){
                    dp.add(i);
                    break;
                }
            }
        }
        if (dp.get(dp.size() - 1) != s.length()) return ans;
        return insert(0, dp.size() - 1, s, wordDict);
    }
    
    public List<String> insert(int start, int end, String s, Set<String> wordDict){
        String string = s.substring(dp.get(start), dp.get(end)), substr;
        //check whether we can get the result form cache directly
        if (map.containsKey(string)) return map.get(string);
        //if couldn't, check whether the whole string in wordDict or not, if yes, add it
        List<String> res = new ArrayList<>();
        if (wordDict.contains(string)) res.add(string);
        //otherwise, try to break it and repeat this process
        for (int i = start + 1; i < end; i++){
            if (wordDict.contains(s.substring(dp.get(start), dp.get(i)))){
                substr = s.substring(dp.get(start), dp.get(i));
                for (String item : insert(i, end, s, wordDict))
                    res.add(substr + ' ' + item);
            }
        }
        map.put(string, res);
        return res;
    }
}
