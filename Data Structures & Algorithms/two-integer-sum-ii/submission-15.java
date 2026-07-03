class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int j = 1;
        int sum = numbers[i] + numbers[j];
        int[] result = new int[2];
        while (sum != target && numbers[i] <= target/2 && j < numbers.length){
            if (j+1 < numbers.length){
                if (numbers[j+1] + numbers[i] <= target){
                    j++;
                }
                else if ( numbers[j+1] + numbers[i] > target && sum <= target){
                    i++;
                }
                else if (numbers[j+1] + numbers[i] > target && sum > target ){
                    j--;
                }            
            }
            else {
                if (sum < target){
                    i++;
                }
                else{
                    j--;
                }
            }
            sum = numbers[i] + numbers[j];
        }
        result = new int[]{i+1, j+1};
        return result;
    }
}
//[0,2,2,3,5]