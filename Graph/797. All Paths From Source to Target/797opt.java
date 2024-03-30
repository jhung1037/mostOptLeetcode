class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        
        return new java.util.AbstractList<List<Integer>>() {
            
            List<List<Integer>> allPaths = null;
            
            Deque<Integer> path = new ArrayDeque<>();
            
            @Override 
            public List<Integer> get(int i) {
                return allPaths.get(i);
            }
            
            @Override 
            public int size() {
                if (allPaths == null) {
                    allPaths = new ArrayList<>();
                    dfs(0);
                }
                return allPaths.size();
            }
            
            private void dfs(int curr) {
                path.addLast(curr);
                if (curr == graph.length-1) {
                    allPaths.add(new ArrayList<>(path));
                } else {
                    for (int v : graph[curr]) {
                        dfs(v);
                    }
                }
                path.pollLast();
            }
        };
    }
}
