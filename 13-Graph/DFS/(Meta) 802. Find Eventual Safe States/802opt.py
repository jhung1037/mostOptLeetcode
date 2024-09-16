class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def loop(node):
            if status[node] != 0 : return status[node] == 2
            # if status[node] == 1: return False
            # if status[node] == 2: return True

            status[node] = 2
            for child in graph[node]:
                if loop(child):
                    return True
            status[node] = 1
            return False

        '''
        state:
        0 -> not checked
        1 -> checked
        2 -> checking
        '''
        n = len(graph)
        status = [0] * n
        res = []
        for i in range(n):
            if not loop(i):
                res.append(i)

        return res
