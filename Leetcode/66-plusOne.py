# encoding: utf-8
# 
# ###################
# 66. Plus One
# Difficulty: Easy
# ###################

# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

# leetcode.com Submission
# 109 / 109 test cases passed.
# Status: Accepted
# Runtime: 56 ms
# Your runtime beats 97.72 % of python3 submissions.


class Solution:
    def plusOne(self, digits):
        """
        思路：要注意审题，在结果数组中的每个元素都只能是单个数字
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return [1]
        else:
            n = len(digits)

            # 确保数组中的每个元素都只有一位数字
            if digits[-1] == 9:
                if n >= 2 and digits[n-2] < 9:
                    # 数组中只有最后一个元素为 9 的情况下，只需要处理最后一个和倒数第二个元素
                    digits[n - 1] = 0
                    digits[n-2] += 1
                    return digits
                elif n < 2:
                    # 数组中只有最后一个元素为 9 的情况下，且数组长度为 1
                    digits[n - 1] = 0
                    digits.insert(0, 1)
                    return digits

            plus_one = 1

            for i in range(n - 1, 0, -1):
                digits[i] += plus_one
                if digits[i] == 10:
                    digits[i] = 0
                    plus_one = 1
                else:
                    plus_one = 0
            digits[0] += plus_one
            if digits[0] == 10:
                digits[0] = 0
                digits.insert(0, 1)
            return digits

# Expected: [1,0]
print(Solution().plusOne([9]))

print(Solution().plusOne([9, 9]))
print(Solution().plusOne([1, 0, 9]))

print(Solution().plusOne([5, 6, 2, 0, 0, 4, 6, 2, 4, 9]))
print(Solution().plusOne([]))
print(Solution().plusOne([0]))
print(Solution().plusOne([1, 2, 3]))
print(Solution().plusOne([4, 3, 2, 1]))