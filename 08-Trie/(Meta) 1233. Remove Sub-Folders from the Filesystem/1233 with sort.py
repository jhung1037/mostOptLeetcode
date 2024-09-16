class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        check = " "
        for f in folder:
            if not f.startswith(check):
                check = f
                res.append(check)
                check += '/'
            
        return res
