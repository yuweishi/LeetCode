public class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<>();
        if (s.length() == 0){ res.add(new ArrayList<String>());return res;}
        for (int i = 1; i <= s.length(); i++){
            String substr = s.substring(0, i);
            if (isPal(substr)){
                for (List<String> list : partition(s.substring(i))){
                    List<String> newlist = new ArrayList<String>(list);
                    newlist.add(0, substr);
                    res.add(newlist);
                }
            }
        }
        return res;
    }
    public boolean isPal(String str){
        int l = 0, r = str.length()-1;
        while(l <= r){
            if(str.charAt(l) != str.charAt(r))  return false;
            l++;r--;
        }
        return true;
    }
}
