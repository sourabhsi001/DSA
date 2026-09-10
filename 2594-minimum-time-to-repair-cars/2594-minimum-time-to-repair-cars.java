class Solution {
    public boolean helper(int[] ranks, int cars,long mid){
        long sum = 0;
        for(int i=0;i<ranks.length;i++){
            sum += (long) Math.pow(mid/ranks[i],0.5);
        }


        return sum>=cars ? true:false;
    }
    public long repairCars(int[] ranks, int cars) {
        long start = 0;
        long max = 0;
        for(int i=0;i<ranks.length;i++){
            max = Math.max(max,ranks[i]);
        }
        long end = 1L * cars*cars * max;
        long ans = end;
        while(start<=end){
            long mid = (start+end)/2;
            if(helper(ranks,cars,mid)){
                end = mid-1;
                ans = Math.min(ans,mid);
            }else{
                start = mid+1;
            }
        }
        return  ans;
    }
}