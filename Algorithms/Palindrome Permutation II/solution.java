public class Solution {
    public List<String> generatePalindromes(String s) {
        HashMap<Character, Integer> dict = new HashMap<>();
        List<String> res = new ArrayList<String>();
        String odd = "", str = "";
        for (int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if (!dict.containsKey(ch)) dict.put(ch, 1);
            else dict.put(ch, dict.get(ch) + 1);
        }
        for (char k: dict.keySet()){
            for (int i = 0; i < dict.get(k) / 2; i++)
                str += "" + k;
            if (dict.get(k) % 2 == 1){
                if (odd.length() == 1) return res;
                odd = "" + k;
            }
        }
        for (StringBuilder p: permuteUnique(str)){
            res.add((p + odd + p.reverse()).toString());
        }
        if (res.size() == 0)
            res.add(odd);
        return res;
    }
    
    public List<StringBuilder> permuteUnique(String nums) {
        List<StringBuilder> res = new ArrayList<>();
        if (nums == null || nums.length() == 0) return res;
        res.add(new StringBuilder());
        for (int i = 0; i < nums.length(); i++){
            List<StringBuilder> newres = new ArrayList<>();
            for (StringBuilder l : res){            
                for (int j = 0; j <= i; j++){
                    if (j > 0 && l.charAt(j - 1) == nums.charAt(i))
                        break;
                    StringBuilder new_l = new StringBuilder(l);
                    new_l.insert(j, nums.charAt(i));
                    newres.add(new_l);
                }
            }
            res = newres;
        }
        return res;
    }
}
