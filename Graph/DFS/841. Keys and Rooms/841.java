class Solution {
    public void go(int room_num, List<List<Integer>> rooms, boolean[] visited){
        visited[room_num] = true;
        for(int key : rooms.get(room_num)){
            if(!visited[key]){
                go(key, rooms, visited);
            }
        }
    }

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] visited = new boolean[rooms.size()];
        go(0, rooms, visited);

        for(boolean status : visited){
            if(!status){return false;}
        }

        return true;
    }
}