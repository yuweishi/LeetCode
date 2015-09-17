public class Solution {
    public boolean isStrobogrammatic(String num) {
        Map<Character, Character> map = new HashMap<Character, Character>();
        map.put('6', '9');
        map.put('9', '6');
        map.put('0', '0');
        map.put('1', '1');
        map.put('8', '8');
        int start = 0, end = num.length() - 1;
        while (start <= end){
            if (!map.containsKey(num.charAt(end)) || num.charAt(start) != map.get(num.charAt(end))){
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}
