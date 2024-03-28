class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        boolean[] seen = new boolean[n];
        boolean edgeVisit = true;
        seen[source] = true;
        while(!seen[destination] && edgeVisit){
            edgeVisit = false;
            for (int[] edge:edges){
                if ( seen[edge[0]] ^ seen[edge[1]] ){
                    seen[edge[0]] = true;
                    seen[edge[1]] = true;
                    if (seen[destination]) return true;
                    
                    edgeVisit = true;
                }
            }
        }
        return seen[destination];
    }
}