class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_khash = {}
        k_maxlist = []
        # nums=[3,0,1,0]
        for num in nums:
            if num not in top_khash:
                top_khash[num] = 1
            else:
                top_khash[num] += 1
        # print(top_khash)
        for times in range(k):
            max_num = [0,0] #num followed by count 
            for x in top_khash:
                if top_khash[x] > max_num[1]:
                    max_num = [x,top_khash[x]]
            top_khash.pop(max_num[0])
            k_maxlist.append(max_num[0])
        
        return k_maxlist
                