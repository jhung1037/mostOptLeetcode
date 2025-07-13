class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # time complexity: O(N^(T/M)) where T is target and M is the smallest num
        # space complexity: O(T/M) where T is target and M is the smallest num
        res = []
        
        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if candidate > remaining:
                    break

                path.append(candidate)
                backtrack(i, path, remaining - candidate)
                path.pop()
        
        candidates.sort()
        backtrack(0, [], target)
        return res
