class Solution:
    def smallestNumber(self, pattern: str) -> str:
        pattern += 'I'
        res = stack = ''
        for i, p in enumerate(pattern):
            stack = str(i+1) + stack
            if p == 'I':
                res += stack
                stack = ''
        return res
