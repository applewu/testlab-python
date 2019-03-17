# encoding: utf-8
#
# ###################
# 165. Compare Version Numbers
# Difficulty:Medium
# ###################
#
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
#
# The . character does not represent a decimal point and is used to separate number sequences.
#
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
#
# You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.
#
#
#
# Example 1:
#
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
#
# Example 2:
#
# Input: version1 = "1.0.1", version2 = "1"
# Output: 1
#
# Example 3:
#
# Input: version1 = "7.5.2.4", version2 = "7.5.3"
# Output: -1
#
# Example 4:
#
# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”
#
# Example 5:
#
# Input: version1 = "1.0", version2 = "1.0.0"
# Output: 0
# Explanation: The first version number does not have a third level revision number, which means its third level revision number is default to "0"
#
#
#
# Note:
#
#     Version strings are composed of numeric strings separated by dots . and this numeric strings may have leading zeroes.
#     Version strings do not start or end with dots, and they will not be two consecutive dots.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        思路：这应该是最常见的处理方式了，根据 "." 分隔符形成两个数组，再比较两者元素的数值大小
        :param version1:
        :param version2:
        :return:

        leetcode.com Submission
        72 / 72 test cases passed.
        Status: Accepted
        Runtime: 52 ms
        Your runtime beats 15.65 % of python3 submissions.
        """
        ver1_array = version1.split('.')
        ver2_array = version2.split('.')
        common_level = len(ver1_array) <= len(ver2_array) and len(ver1_array) or len(ver2_array)
        for l in range(common_level):
            ver1_num = int(ver1_array[l])
            ver2_num = int(ver2_array[l])
            if ver1_num > ver2_num:
                return 1
            elif ver1_num < ver2_num:
                return -1

        if len(ver1_array) == len(ver2_array) == common_level:
            return 0
        elif len(ver1_array) == common_level:
            for i in range(len(ver2_array)-1, common_level-1, -1):
                if int(ver2_array[i]) > 0:
                    return -1
            return 0
        elif len(ver2_array) == common_level:
            for i in range(len(ver1_array)-1, common_level-1, -1):
                if int(ver1_array[i]) > 0:
                    return 1
            return 0




print(Solution().compareVersion(version1="0.1", version2="1.1"))
print(Solution().compareVersion(version1="1.0.1", version2="1"))
print(Solution().compareVersion(version1="7.5.2.4", version2="7.5.3"))
print(Solution().compareVersion(version1="1.01", version2="1.001"))
print(Solution().compareVersion(version1="1.0", version2="1.0.0"))
print(Solution().compareVersion(version1="1", version2="1.1"))
print(Solution().compareVersion(version1="1.0.0", version2="1.0"))