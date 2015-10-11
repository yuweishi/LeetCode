public class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        List<List<String>> result = new ArrayList<List<String>>();
        Map<String, List<String>> map = new HashMap<String, List<String>>();
        for (String str: strings){
            String key = "";
            for (int i = 0; i < str.length(); i++) key += (char) ((str.charAt(i) - str.charAt(0) + 26) % 26 + 97);
            if (!map.containsKey(key)) map.put(key, new ArrayList<String>());
            map.get(key).add(str);
        }
        for (List<String> value : map.values()) {
            Collections.sort(value);
            result.add(value);
        }
        return result;
    }
}
