class Solution {
    public void go(int city, int[][] isConnected, boolean[] visited){
        int N = isConnected[city].length;
        for(int i = 0; i < N; i++){
            if(i != city && !visited[i] && isConnected[city][i]==1){
                visited[i] = true;
                go(i, isConnected, visited);
            }
        }
    }

    public int findCircleNum(int[][] isConnected) {
        int N = isConnected.length;
        boolean[] visited = new boolean[N];
        int provinces = 0;

        for(int i = 0; i < N; i++){
            if(!visited[i]){
                provinces ++;
                visited[i] = true;
                go(i, isConnected, visited);
            }
        }

        return provinces;
    }
}