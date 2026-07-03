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
        return dict1.equals(dict2);    
    }  
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        Map<String,Integer> visited = new HashMap<>();
        for (int i = 0; i < strs.length; i++){
            List<String> liste = new ArrayList<>();
            if (!visited.containsKey(strs[i])){
                visited.put(strs[i],1);
                liste.add(strs[i]);
                for (int j = i+1; j < strs.length; j++){
                    System.out.println(isAnagram(strs[i],strs[j]));
                    if (isAnagram(strs[i],strs[j]) | strs[i] == strs[j]){
                        liste.add(strs[j]);
                        visited.put(strs[j],2);
                    }
                }
                result.add(liste);
                System.out.println(visited);
            }


        }
        return result;

    }
}
