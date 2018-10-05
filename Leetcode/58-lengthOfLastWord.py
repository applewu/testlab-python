# encoding: utf-8
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5

class Solution:
    def lengthOfLastWord(self, s):
        """
        思路：空格是决定是否是最后一个字符串的关键因素。把空格的位置，是否存在空格作为判断条件。
        :type s: str
        :rtype: int
        """
        result = 0

        if ' ' in s:
            last_space_index = s.rindex(' ')
            result = len(s[last_space_index+1:])
            if result == 0:
                result = self.lengthOfLastWord(s[:last_space_index])
        else:
            result = len(s)
        
        return result

print(Solution().lengthOfLastWord(s='Hello World'))
print(Solution().lengthOfLastWord(s='Hello World Shanghai '))
print(Solution().lengthOfLastWord(s='a'))
print(Solution().lengthOfLastWord(s='a '))
print(Solution().lengthOfLastWord(s=''))
print(Solution().lengthOfLastWord(s=' '))