class Solution {
    public int getWinner(int[] arr, int k) {
        //Base or Cornor Case
        if(k==1) return Math.max(arr[0], arr[1]);
        if(k >= arr.length) {
            //Returning the maximum Element..... 
            Arrays.sort(arr);
            return arr[arr.length-1];

         // return Arrays.stream(arr).max().getAsInt();
        }


        int prev = arr[0];
        int wins=0;
        for(int i=1; i<arr.length; i++){
            if(prev > arr[i]){
                wins++;
            } else{
                prev = arr[i];
                wins=1;
            }

            if(wins == k){
                return prev;
            }
        }
        
        return prev;
    }
}