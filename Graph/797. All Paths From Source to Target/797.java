import java.util.ArrayList;

class Solution {
    public List<List<Integer>> ans = new ArrayList<>();

    public void go(int start, List<Integer> lis, int end, int[][] graph){
        if(start == end){
            lis.add(end);
            ans.add(new ArrayList<>(lis));
            lis.remove(lis.size()-1);
            return;
        }

        lis.add(start);
        for(int des : graph[start]){
            go(des, lis, end, graph);
        }
        lis.remove(lis.size()-1);

    }

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        int end = graph.length - 1;
        go(0, new ArrayList<>(), end, graph);
        return ans;
    }
}