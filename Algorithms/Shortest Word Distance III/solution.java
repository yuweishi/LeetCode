public class Solution {
    public int shortestWordDistance(String[] words, String word1, String word2) {
        int distance = Integer.MAX_VALUE, p1 = -1, p2 = -1;
        boolean same = word1.equals(word2);
        System.out.printf("%b", same);
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(word1) && (!same || p1 < p2)) {
                p1 = i;
            }
            else if (words[i].equals(word2)) {
                p2 = i;
            }
            if (p1 != -1 && p2 != -1) {
                distance = Math.min(distance, Math.abs(p2 - p1));
            }
        }
        return distance;
    }
}
