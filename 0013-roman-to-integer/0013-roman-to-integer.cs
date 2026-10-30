public class Solution {
    public int RomanToInt(string s) {
        Dictionary<char,int> d = new Dictionary<char,int>(){['I']=1,['V']=5,['X']=10,['L']=50,['C']=100, ['D']=500,['M']=1000};
        int Total=0;
        int n=s.Length-1;
        for(int i = 0 ; i <= n ; i++ ) {
            if ((i+1 <= n) && d[s[i]] < d[s[i+1]]) {
                Total-=d[s[i]];
            }
            else {
                Total+=d[s[i]];
            }
            
        }
        return Total;
        
    }
}