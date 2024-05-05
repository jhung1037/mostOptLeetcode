class Solution:
    def start_z(self, tri):
        return True if len(tri)>=2 and tri[0] == '0' else False
        
    def overflow(self, tri):
        if not tri: return False
        return True if int(tri) > 255 else False

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12: return []

        def recur(lis, count):
            if not lis : return []
            if count == 4:
                return [] if self.start_z(lis) or self.overflow(lis) else [lis]

            res = []
            for i in range(3):
                poss = []
                ip = lis[:i+1]
                if self.start_z(ip) or self.overflow(ip): continue

                perm = recur(lis[i+1:], count+1)
                if not perm: continue
                for p in perm:
                    poss.append(ip + '.' + p)
                res.extend(poss)
            return res
        
        return recur(s, 1)
