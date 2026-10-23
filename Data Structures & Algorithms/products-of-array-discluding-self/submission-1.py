class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initializing prefix and suffix lists  
        prefix = [1] * n  
        suffix = [1] * n  

        # Computing prefix products  
        for i in range(1, n):  
            prefix[i] = prefix[i - 1] * nums[i - 1]  

        # Computing suffix products  
        for i in range(n - 2, -1, -1):  
            suffix[i] = suffix[i + 1] * nums[i + 1]  

        # Getting final suffix product by multiplying prefix and suffix  
        result = [prefix[i] * suffix[i] for i in range(n)]  

        return result
                



        