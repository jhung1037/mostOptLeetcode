class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def find(log):
            i, s = log.split(" ", maxsplit=1)
            return (1, ) if s[0].isdigit() else (0, s, i)
        logs.sort(key=find)
        return logs