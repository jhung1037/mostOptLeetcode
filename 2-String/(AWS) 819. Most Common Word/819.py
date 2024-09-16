class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        b = set(banned)

        dic = collections.defaultdict(int)
        res = ""
        s = ""
        p = paragraph.lower() + " "
        for c in p:
            if c.isalpha():
                s += c
            elif s != "":
                if s not in b:
                    dic[s] += 1
                    if dic[s] > dic[res]:
                        res = s
                s = ""
        return res