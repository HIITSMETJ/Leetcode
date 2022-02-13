// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set=[[]]
        for i in nums:
            tmp=[sub_set+[i] for sub_set in power_set]
            power_set+=tmp
        return power_set    