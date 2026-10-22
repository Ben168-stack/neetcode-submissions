class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_hash = {}
        for i in nums:
            if i not in nums_hash:
                nums_hash[i] = 1
            else:
                nums_hash[i] += 1
                return True
        return False
        
        # for x in nums_hash:
             
        #     if nums_hash[x] > 1:
        #         return True
        # return False
               