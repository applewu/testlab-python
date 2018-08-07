# encoding: utf-8
# The string  is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
# Example 1:
#
# Input: s = c, numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


class Solution(object):
    def convert(self, s, numRows):
        """
        思路：有两种特殊情况，是字符串长度或者行数是1，均直接返回原字符串。其他情况的处理逻辑是：
        Z 字形打印，可以看作将原字符串形成了多个 V 形分组，再打印出来。
        例如："PAHNAPLSIIGYIR" 在行数为 3 的情况下，分组为：PAYP，ALIS，HIRI，NG
        "PAHNAPLSIIGYIR" 在行数为 4 的情况下，分组为：PAYPAL，ISHIRI，NG
        :type s: str
        :type numRows: int
        :rtype: str
        """
        i = 0
        fz = numRows * 2 - 2  # V 形分组处理，fz 是单个组的元素个数

        result = ''

        if (numRows == 1) | (len(s) == 1):
            return s

        while i < numRows:
            j = 0
            # j 是组的个数
            while (i + j * fz) < len(s):
                result += s[i + j * fz]
                # V 形分组，若不是首行或尾行，则该行会输出两个字符
                another_index = i + fz - i * 2
                if (i != 0) & (i != numRows - 1) & ((another_index + j * fz) < len(s)):
                    result += s[another_index + j * fz]
                j += 1
            i += 1
        return result


print Solution().convert(s='PAYPALISHIRING', numRows=4)
print Solution().convert(s='PAYPALISHIRING', numRows=3)
