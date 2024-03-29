class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        boolean[] seen = new boolean[n];
        seen[source] = true;
        boolean thorough = false;
        while(!seen[destination] && !thorough){
            thorough = true;
            for(int[] edge : edges){
                if(seen[edge[0]] ^ seen[edge[1]]){
                    seen[edge[0]] = true;
                    seen[edge[1]] = true;
                    if(seen[destination]){return true;}
                    thorough = false;
                }
            }
        }
        return seen[destination];
    }
}