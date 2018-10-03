# encoding: utf-8
# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3
# Example 2:

# Input: [3,4,-1,1]
# Output: 2
# Example 3:

# Input: [7,8,9,11,12]
# Output: 1

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        else:
            nums = sorted(nums)
            if max(nums) <= 0:
                return 1    
            for i in range(1, max(nums)):
                if i not in nums:
                    return i
                else:
                    i += 1

            # 如果没有在 for 循环中返回结果，说明 nums 中没有缺少正数，那么第一个缺少的正数就是最大数的下一个正数
            return max(nums)+1

print(Solution().firstMissingPositive(nums=[1,2,0]))
print(Solution().firstMissingPositive(nums=[3,4,-1,1]))
print(Solution().firstMissingPositive(nums=[7,8,9,11,12]))