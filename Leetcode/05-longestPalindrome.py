# encoding: utf-8
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"


class Solution(object):
    def longestPalindrome(self, s):
        """
        思路：
        1. 先形成回文子串的数组，再找到最长的回文子串
        2. 循环 s，假设循环变量所在位置的字符是回文子串的中心位置，根据回文字符串的特征，找到左右边界，进行切片
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        result = ''
        subs = []

        for i in range(len(s) - 1):
            sub = self.palindrome(s, i)
            if (len(sub) > 0) & (sub not in subs):
                subs.append(sub)

        for f in subs:
            if len(f) > len(result):
                result = f

        return result

    def palindrome(self, s, mid):
        """
        返回回文子串
        :param s: str
        :param mid: int
        :return: sub string
        """
        left = mid - 1 if (mid - 1) >= 0 else mid
        right = mid + 1 if (mid + 1) < len(s) else mid
        while (s[mid] == s[right]) & (right + 1 < len(s)):
            right += 1
        while (left - 1 >= 0) & (right + 1 < len(s)) & (s[left] == s[right]):
            if s[left - 1] != s[right + 1]:
                break
            else:
                left -= 1
                right += 1

        if s[right] == s[left]:
            return s[left:right + 1]
        elif (s[mid] == s[right - 1]) & (s[mid] != s[right]):
            return s[mid:right]
        elif s[mid] == s[right]:
            return s[mid:right + 1]
        else:
            return ''



s_array = ['abb', 'bbbc', 'cfdcaaac', 'bb', 'bbb', 'babad', 'cbbd', 'a', 'ac', 'abcda', 'bbbb', 'aba', 'abcba',
           'babadada', '222020221',
           "cwziydanrqvsdtvnnqgjnbrvvwxwqojeqgxhwxdoktjktulemwpbeqscbbtbfvkxsrjetfdrovcrdwzfmnnihtgxybuairswfewvpuscocqifuwylhssldpjrawqdrbvkykpaggspbfrulcktpbofchzikhzxhpocgvdbwpewpywsgqbczmamprklaoovcfecwchhmsaqkhvuvvzjblmgvqpqtnlipgqsanvovylpmxlmxvymppdykphhaamtxjnnlsqfwjwhyywgurteaummwhvavxbcpgrfffxrowluqmqjaugryxdmwvyokdcfcvcytxpixbvwrdgzctejdoaavgtezexmvxgrkpnayvfarkyoruofqmpnsqdzojxqrjsnfwsbzjmaoigytygukqlrcqaxazvmytgfghdczvzphfdbnxtklaiqqsotavdmhiaermluafheowcobjqmrkmlzyas"
           ]
for s in s_array:
    print Solution().longestPalindrome(s)
