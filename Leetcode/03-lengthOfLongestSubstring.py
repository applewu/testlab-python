# encoding: utf-8
# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        substr_final = ''  # 最终返回的最长 substring
        substr = ''
        while (i < len(s)):

            if (substr.find(s[i]) < 0):
                substr = substr + s[i]

                if len(substr) > len(substr_final):
                    substr_final = substr
            elif (len(substr) > 1):
                start = substr.index(s[i]) + 1  # 若出现重复字符，则从该字符后面的位置开始截取
                substr = substr[start:] + s[i]
            else:
                substr = s[i]
            i = i + 1
        # print substr_final
        return len(substr_final)


s = Solution()
print s.lengthOfLongestSubstring("ohvhjdml")
