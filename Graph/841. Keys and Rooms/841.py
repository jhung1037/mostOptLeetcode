class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def go(room_num):
            visited.add(room_num)
            for key in rooms[room_num]:
                if key not in visited:
                    go(key)

        go(0)

        return len(visited) == len(rooms)
