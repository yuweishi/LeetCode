public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for(String s : strs) {
            res.append(s.length()).append('/').append(s);
        }
        return res.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        ArrayList<String> res = new ArrayList<String>();
        int i = 0, i1, len;
        while (i < s.length()){
            i1 = s.indexOf('/', i);
            len = Integer.valueOf(s.substring(i, i1));
            res.add(s.substring(i1 + 1, i1 + len + 1));
            i = i1 + len + 1;
        }
        return res;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));
