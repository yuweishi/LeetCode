public class ValidWordAbbr {
    HashMap<String, HashSet<String>> map = new HashMap<String, HashSet<String>> ();
    public ValidWordAbbr(String[] dictionary) {
        for (String word: dictionary) {
            int len = word.length();
            String abbr = word.substring(0, 1) + (len - 2) + word.substring(len - 1);
            if (map.containsKey(abbr)) map.get(abbr).add(word);
            else{
                HashSet<String> item = new HashSet<String> ();
                item.add(word);
                map.put(abbr, item);
            }
        }
    }

    public boolean isUnique(String word) {
        int len = word.length();
        String abbr = word.substring(0, 1) + (len - 2) + word.substring(len - 1);
        if (map.containsKey(abbr) && (map.get(abbr).size() > 1 || !map.get(abbr).contains(word))) return false;
        return true;
    }
}


// Your ValidWordAbbr object will be instantiated and called as such:
// ValidWordAbbr vwa = new ValidWordAbbr(dictionary);
// vwa.isUnique("Word");
// vwa.isUnique("anotherWord");
