public class Solution {
    public String minWindow(String s, String t) {
        if (s.length() == 0 || t.length() == 0) {
            return "";
        }
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int start = 0, end = Integer.MAX_VALUE, count = t.length(), i = 0, j;
        for (int k = 0; k < t.length(); k++) {
            char cur = t.charAt(k);
            if (map.containsKey(cur)) {
                map.put(cur, map.get(cur) + 1);
            }
            else {
                map.put(cur, 1);
            }
        }
        for (j = 0; j < s.length(); j++) {
            char cur = s.charAt(j);
            if (map.containsKey(cur)) {
                if (map.get(cur) > 0) {
                    count--;
                }
                map.put(cur, map.get(cur) - 1);
            }
            while (i < j && !(map.containsKey(s.charAt(i)) && map.get(s.charAt(i)) >= 0)) {
                if (map.containsKey(s.charAt(i))) {
                    map.put(s.charAt(i), map.get(s.charAt(i)) + 1);
                }
                i++;
            }
            if (count == 0 && end - start > j - i) {
                end = j;
                start = i;
            }
        }
        return count > 0 ? "" : s.substring(start, end + 1);
    }
}
