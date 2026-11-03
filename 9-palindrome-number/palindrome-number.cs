public class Solution {
    public bool IsPalindrome(int x) {
        if(x <0) {
            return false;
        }
        int n = x;
        int b=0;
        while(n>0) {
            int rem=n%10;
            b=b*10+rem;
            n/=10;
        }
        if (b==x) {
            return true;
        }
        return false;
        
    }
}