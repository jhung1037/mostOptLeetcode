class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        boolean[] visited = new boolean[n];
        List<Integer> ans = new ArrayList<>();
        int size = edges.size();
        for(int i = 0; i < size; i++){
            visited[edges.get(i).get(1)] = true;
        }
        
        for(int i = 0; i < n; i++){
            if(visited[i] == false){
                ans.add(i);
            }
        }

        return ans;
    }
}