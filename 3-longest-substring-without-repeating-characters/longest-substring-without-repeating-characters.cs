public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int n=s.Length;
        if (n <=1) {
            return n;
        }
        int maxLength=1;
        int l=0;
        Dictionary<char,int> lastSeen= new Dictionary<char,int>();
        for (int i=0; i< n ;i++) {
            if ((lastSeen.ContainsKey(s[i])) && (lastSeen[s[i]] >= l)) {
                l=lastSeen[s[i]]+1;
                    
            }
            maxLength= Math.Max(maxLength,i-l+1);
            lastSeen[s[i]]=i;
        }
        return maxLength;
    }
}