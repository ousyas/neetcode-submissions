class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer,Integer> dict = new HashMap<>();
        int i = 0;
        boolean result = false;
        while (i < nums.length && result == false){
            if (dict.containsKey(nums[i])){
                result = true;
            }
            dict.put(nums[i],1);
            System.out.println(nums[i]);
            i++;
        } 
        return result; 
    }
}