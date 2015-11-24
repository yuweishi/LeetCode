public class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        int n = words.length, start = 0;
        List<String> res = new LinkedList<String>();
        while (start < n) {
            int count = 0, total = words[start].length();
            while (start + count + 1 < n && total + count + words[start + count + 1].length() + 1 <= maxWidth) {
                total += words[start + 1 + count++].length();
            }
            StringBuilder sb = new StringBuilder(words[start]);
            if (start + count + 1 != n && count != 0) {
                int base = (maxWidth - total) / count;
                int left = (maxWidth - total) % count;
                for (int i = start + 1; i <= start + count; i++) {
                    if (i < start + left + 1) {
                        sb.append(" ");
                    }
                    for (int j = 0; j < base; j++) {
                        sb.append(" ");
                    }
                    sb.append(words[i]);
                }
            }
            else {
                for (int i = start + 1; i <= start + count; i++) {
                    sb.append(" ").append(words[i]);
                }
                for (int j = 0; j < maxWidth - total - count; j++) {
                    sb.append(" ");
                }
            }
            res.add(sb.toString());
            start += count + 1;
        }
        return res;
    }
}
