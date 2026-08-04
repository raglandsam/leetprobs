class Solution {
    public int[] replaceElements(int[] arr) {
        if( arr.length == 1){
            return new int[] {-1};
        }
        int maxsofar = arr[arr.length-1];
        arr[arr.length-1] = -1;
        for ( int i = arr.length-2; i>=0; i--) {
            int element = arr[i];
            arr[i] = maxsofar;
            if ( element > maxsofar) {
                maxsofar= element;
            }
        
        }
        return arr;

    }
}