class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        price = [math.inf] * n
        price[src] = 0

        for i in range(k+1):
            temp = price.copy()

            for u,v,w in flights:
                if price[u] != math.inf:
                    temp[v] = min(price[u]+w, temp[v])
            
            price = temp

        return price[dst] if price[dst] != math.inf else -1
