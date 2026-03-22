# O(n^2)
class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                s = nums[i]+nums[j]
                if s < target:
                    count+=1
        return count
                
