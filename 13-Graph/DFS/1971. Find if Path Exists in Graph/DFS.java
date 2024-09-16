import java.util.*;

class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        HashMap<Integer, ArrayList<Integer>> link = new HashMap<>();
        for(int[] edge : edges){
            link.computeIfAbsent(edge[0], k -> new ArrayList<>()).add(edge[1]);
            link.computeIfAbsent(edge[1], k -> new ArrayList<>()).add(edge[0]);
        }

        boolean[] visited = new boolean[n];
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.addFirst(source);

        while(!queue.isEmpty()){
            int node = queue.poll();
            if(node == destination){return true;}
            if(!visited[node]){
                visited[node] = true;
                for(int neighbor : link.get(node)){
                    if(!visited[neighbor]){
                        queue.addLast(neighbor);
                    }
                }
            }
        }

        return false;
    }
}