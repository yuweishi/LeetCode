public class Solution {
    public String getHint(String secret, String guess) {
        int count1 = 0, count2 = 0;
        int[] map = new int[10];
        for (int i = 0; i < secret.length(); i++) {
            if (secret.charAt(i) == guess.charAt(i))
                count1++;
            else {
                if (map[secret.charAt(i) - '0']++ < 0)
                    count2++;
                if (map[guess.charAt(i) - '0']-- > 0)
                    count2++;
            }
        }
        return count1 + "A" + count2 + "B";
    }
}
