public class Solution {
    public void reverseWords(char[] s) {
        int start = 0, end = 0, n = s.length - 1, temp;
        char temp1;
        while (start < n) {
            while (end < n && s[end + 1] != ' ') end++;
            temp = end + 2;
            while (start < end){
                temp1 = s[start];
                s[start] = s[end];
                s[end] = temp1;
                start++;
                end--;
            }
            start = end = temp;
        }
        start = 0; 
        end = n;
        while (start < end){
            temp1 = s[start];
            s[start] = s[end];
            s[end] = temp1;
            start++;
            end--;
        }
    }
}
