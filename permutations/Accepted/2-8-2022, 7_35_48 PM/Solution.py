// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        per=[]
        if len(nums)<2:
            return [nums]
        else:
            a = nums[0]
            tmp = self.permute(nums[1:])
            for i in range(len(nums)):
                for l in tmp:
                    per.append(l[:i] + [a] + l[i:])
        return per        
        
            
            
            
        