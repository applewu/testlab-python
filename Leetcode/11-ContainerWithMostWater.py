# encoding: utf-8
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
# Example:
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49


class Solution(object):
    def maxArea(self, height):
        """
        思路：
        1. 从数组的两边往中间找，所求面积的长是两元素位置之差，高是两元素值中较小的;
        2. 无需关心元素位置信息，只需要输出最大面积的值。
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            w = j - i

            if height[i] > height[j]:
                h = height[j]
                j -= 1

            else:
                h = height[i]
                i += 1

            max_area = max(max_area, w * h)

        return max_area


print Solution().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])
