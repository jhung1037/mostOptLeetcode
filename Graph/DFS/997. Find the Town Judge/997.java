class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] people = new int[n+1];
        for(int[] pair : trust){
            people[pair[0]]--;
            people[pair[1]]++;
        }
        for(int i=1; i<=n; i++){
            if(people[i] >= n-1) return i;
        }
        return -1;
    }
}