class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_k = 1
        max_k = max(piles)
        while low_k < max_k:
            k = (low_k+max_k)//2
            hours = 0
            for x in piles:
                hours += (x + k - 1)//k

            if hours <= h:
                max_k = k        
            else:
                low_k = k + 1 

        return low_k
        