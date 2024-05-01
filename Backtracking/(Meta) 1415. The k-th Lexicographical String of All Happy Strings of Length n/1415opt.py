class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        lv = 3 * 2 ** (n - 1)
        if k > lv: return ''

        lv //= 3
        k -= 1
        char = ['a','b','c']
        s = char[k // lv]
        k %= lv
        n -= 1

        while n > 0:
            options = [c for c in char if c != s[-1]]
            lv //= 2
            s += options[k // lv]
            k %= lv
            n -= 1

        return s
