# encoding:utf-8
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1
# Example 3:
#
# Input: [1,3,5,6], 7
# Output: 4
# Example 4:
#
# Input: [1,3,5,6], 0
# Output: 0


class Solution(object):
    def searchInsert(self, nums, target):
        """
        思路：对于不在数组中的元素，将它的值减1，采用递归的方式去找它应该在的位置
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif target not in nums:
            if target > nums[len(nums) - 1]:
                return len(nums)
            elif target < nums[0]:
                return 0
            else:
                i = self.searchInsert(nums, target - 1)
                if target > nums[i]:
                    return i + 1
                else:
                    return i
        else:
            target_index = nums.index(target)
            return target_index


print(Solution().searchInsert([1, 3, 5, 6], 5))
print(Solution().searchInsert([1, 3, 5, 6], 2))
print(Solution().searchInsert([1, 3, 5, 6], 7))
print(Solution().searchInsert([1, 3, 5, 6], 0))
print(Solution().searchInsert([1, 3, 5, 6, 12, 18, 35], 32))
