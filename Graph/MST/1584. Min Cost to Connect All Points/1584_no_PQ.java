class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        boolean[] visited = new boolean[n];
        int[] minCost = new int[n];
        Arrays.fill(minCost, Integer.MAX_VALUE);
        minCost[0] = 0; int prevPoint = 0;
        int res = 0;
        for (int k = 0; k < n; k++) {
            int minCostIndex = -1;
            for (int i = 0; i < n; i++) {
                if (visited[i]) continue;
                minCost[i] = Math.min(distance(points, prevPoint, i), minCost[i]);
                if (minCostIndex == -1) {
                    minCostIndex = i;
                } else if (minCost[i] < minCost[minCostIndex]) {
                    minCostIndex = i;
                }
            }
            visited[minCostIndex] = true;
            res += minCost[minCostIndex];
            prevPoint = minCostIndex;
        }
        return res;
    }

    public int distance(int[][] points, int i, int j) {
        return Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
    }
}