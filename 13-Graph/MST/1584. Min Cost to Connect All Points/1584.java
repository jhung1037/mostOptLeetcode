class Solution {
    public int minCostConnectPoints(int[][] points) {
        int N = points.length;

        Set<Integer> rest = new HashSet<>();
        for (int i = 0; i < N; i++) {
            rest.add(i);
        }

        int[] shortestD = new int[N];
        Arrays.fill(shortestD, Integer.MAX_VALUE);

        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        minHeap.offer(new int[]{0, 0});

        int ans = 0;

        while(!rest.isEmpty()){
            int[] pair = minHeap.poll();
            int d = pair[0];
            int u = pair[1];
            if (!rest.contains(u)) {continue;}
            rest.remove(u);
            ans += d;
            int x1 = points[u][0];
            int y1 = points[u][1];
            for (int v : rest) {
                int x2 = points[v][0];
                int y2 = points[v][1];
                d = Math.abs(x1 - x2) + Math.abs(y1 - y2);
                if (d < shortestD[v]) {
                    shortestD[v] = d;
                    minHeap.add(new int[]{d, v});
                }
            }
        }
        return ans;
    }
}