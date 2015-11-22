public class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        if (s == null || s.length() == 0 || words == null || words.length == 0) {
            return new LinkedList<Integer>();
        }
        int n = words[0].length();
        HashMap<String, Integer> Origin = new HashMap<String, Integer>();
        List<Integer> res = new LinkedList<Integer>();
        for (String word: words) {
            if (Origin.containsKey(word)) 
                Origin.put(word, Origin.get(word) + 1);
            else
                Origin.put(word, 1);
        }
        for (int i = 0; i < n; i++) {
            int start = i, missing = words.length;
            HashMap<String, Integer> map = new HashMap<String, Integer>();
            for (int end = i; end <= s.length() - n; end += n) {
                String cur = s.substring(end, end + n);
                if (Origin.containsKey(cur)) {
                    missing--;
                    if (map.containsKey(cur)) 
                        map.put(cur, map.get(cur) + 1);
                    else
                        map.put(cur, 1);
                    while (map.get(cur) > Origin.get(cur)) {
                        map.put(s.substring(start, start + n), map.get(s.substring(start, start + n)) - 1);
                        missing++;
                        start += n;
                    }
                    if (missing == 0) {
                        res.add(start);
                    }
                }
                else {
                    start = end + n;
                    missing = words.length;
                    map = new HashMap<String, Integer>();
                }
            }
        }
        return res;
    }
}	
