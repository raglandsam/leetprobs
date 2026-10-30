public class Solution {
    public int MaxArea(int[] height) {
        int l=0;
        int r= height.Length-1;
        int maxWater=0;
        while (l<r) {
            int minHeigth = Math.Min(height[l],height[r]);
            int breadth= r-l;
            maxWater= Math.Max(maxWater, minHeigth*breadth);
            if( height[l] <height[r]) {
                l+=1;
            } else {
                r-=1;
            }           
        }
        return maxWater; 
    }
}