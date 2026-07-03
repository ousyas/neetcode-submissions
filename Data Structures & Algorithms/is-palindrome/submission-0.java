class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length()-1;
        while (i < s.length() && j >= 0){
            char point1 = s.charAt(i);
            char point2 = s.charAt(j);
            if (!Character.isLetterOrDigit(point1)){
                i++;
            }
            else if(!Character.isLetterOrDigit(point2)){
                j--;
            }
            else{
                if (Character.toLowerCase(point1) != Character.toLowerCase(point2)){
                    return false;
                }
                i++;
                j--;
            } 
        }
        return true;

    }
}
