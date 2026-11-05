public class Solution {
    public int[] TwoSum(int[] nums, int target) {
            Dictionary<int,int> myDict= new Dictionary<int,int>();
            
            for (int i=0;i< nums.Length;i++)
            {
            
                if(myDict.ContainsKey(target - nums[i]))
                {
                    return new int[] { myDict[target - nums[i]], i };
                }
                myDict[nums[i]] = i;
            }   
        return new int[] {-1,-1};     
    }
}