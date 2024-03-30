class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1
        ans = []

        def go(start, lis):
            if start == end:
                ans.append(lis+[start])
                return
            
            lis.append(start)
            for des in graph[start]:
                go(des, lis)
            lis.pop()

        go(0,[])

        return ans
