class Solution {
    public int[] productExceptSelf(int[] nums) {
        Map<Integer,Integer> dict = new HashMap<>();
        int product = 1;
        int nbzero = 0;
        int index = 0;
        int[] result = new int[nums.length];
        for(int i = 0; i < nums.length; i++ ){
            dict.put(nums[i],1);
            if (nums[i] != 0){
                product = product*nums[i];
            }
            else {
                nbzero++;
                index = i;
            }
        }
        if (nbzero > 1 ){
            for(int i = 0; i < nums.length; i++ ){
                result[i] = 0;
            }
        }else if(nbzero == 1){
            for(int i = 0; i < nums.length; i++){
                if(i == index){
                    result[i] = product;
                }else{
                    result[i] = 0;
                }
            }
        }else{
            for(int i = 0; i < nums.length; i++){
                result[i] = product / nums[i];
            }
        }
        return result;       
    }
}  
