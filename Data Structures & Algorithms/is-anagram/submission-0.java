class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        Map<Character, Integer> dict1 = new HashMap<>();
        Map<Character, Integer> dict2 = new HashMap<>();
        int i = 0;
        while (i < s.length()){
            if(dict1.containsKey(s.charAt(i))){
                dict1.put(s.charAt(i),dict1.get(s.charAt(i))+1);
            }
            else if (!dict1.containsKey(s.charAt(i))){
               dict1.put(s.charAt(i),1); 
            }
            if(dict2.containsKey(t.charAt(i))){
                dict2.put(t.charAt(i),dict2.get(t.charAt(i))+1);
            }
            else if (!dict2.containsKey(t.charAt(i))){
               dict2.put(t.charAt(i),1); 
            }
            i++;
        }
        System.out.println(dict1);
        System.out.println(dict2);
        return dict1.equals(dict2);    
    }  
}
