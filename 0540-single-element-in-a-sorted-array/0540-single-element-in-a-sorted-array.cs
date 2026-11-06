public class Solution {
    public int SingleNonDuplicate(int[] nums) {
        if (nums.Length==1) {
            return nums[0];
        }
        for(int i=0; i<nums.Length;i++) {
            if((i<nums.Length-1) && (nums[i]==nums[i+1])){
                i+=1;
            }
            else{
                return nums[i];
            }
        }
        return -1;     
    }
}