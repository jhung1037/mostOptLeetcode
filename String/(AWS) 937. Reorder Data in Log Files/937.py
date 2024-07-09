class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        res = []
        dig = []
        hp = []
        for log in logs:
            for i, c in enumerate(log):
                if c == ' ':
                    if log[i+1].isdigit():
                        dig.append(log)
                    else:
                        heapq.heappush(hp, (log[i+1:],log[:i],log))
                    break

        while hp:
            res.append(heapq.heappop(hp)[2])

        res.extend(dig)
        return res