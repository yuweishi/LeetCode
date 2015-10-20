public class Solution {
    public boolean wordPatternMatch(String pattern, String str) {
        HashMap<Character, String> dict = new HashMap<>(); 
        HashSet<String>set = new HashSet<>();
        return match(pattern, str, 0, 0, dict, set);
    }
    public boolean match(String pattern, String str, int index, int start, HashMap<Character, String> dict, HashSet<String>set){
        //reach the end, return True
        if (start == str.length() && index == pattern.length()) return true;
        //cannot reach the end at the same time, return False
        if (index == pattern.length() || str.length() - start < pattern.length() - index) return false;
        //check if current pattern already exist
        char cur_pattern = pattern.charAt(index);
        //if exist, check whether match
        if (dict.containsKey(cur_pattern)){
            String p = dict.get(cur_pattern);
            if (!str.startsWith(p, start))
                return false;
            return match(pattern, str, index + 1, start + p.length(), dict, set);
        }
        //otherwise, try to find a new pattern
        for (int end = start + 1; end < str.length() + 1; end++){
            String substr = str.substring(start, end);
            //check whether a substr may refer to two different pattern
            if (!set.contains(substr)){
                dict.put(cur_pattern, substr);
                set.add(substr);
                if (match(pattern, str, index + 1, end, dict, set))
                    return true;
                dict.remove(cur_pattern);
                set.remove(substr);
            }
        }
        return false;
    }
}
