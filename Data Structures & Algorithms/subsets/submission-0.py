class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for i in nums:
            subsets += [curr + [i] for curr in subsets]
        return subsets        