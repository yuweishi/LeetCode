public class Solution {
    //Method 1: brute force
    public int strStr(String haystack, String needle) {
        if (haystack == null || needle == null) {
            return -1;
        }
        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
            for (int j = 0; j <= needle.length(); j++) {
                if (j == needle.length())
                    return i;
                if (needle.charAt(j) != haystack.charAt(i + j))
                    break;
            }
        }
        return -1;
    }

    //Method 2: KMP
    public int strStr(String haystack, String needle) {
	if (haystack == null || needle == null) {
            return -1;
        }
        int i = -1, j = 0, m = haystack.length(), n = needle.length();
        int[] next = new int[n];
        if (next.length > 0) {
            next[0] = -1;
        }
        while (j < n - 1) {
            if (i == -1 || needle.charAt(i) == needle.charAt(j)) {
                next[++j] = ++i;
            }
            else {
                i = next[i];
            }
        }
        i = 0; j = 0;
        while (i < m && j < n) {
            if (j == -1 || haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;
            }
            else {
                j = next[j];
            }
        }
        if (j == n) {
            return i - j;
        }
        return -1;
    }
}
