public class Solution {
    public int MinMoves(int[] nums) {
        int maxElement= nums.Max();
        int maxMoves =0;
        for(int i=0;i<nums.Length;i++) {
            maxMoves+=maxElement - nums[i];
        }        
    return maxMoves;
    }
}