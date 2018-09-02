'''
Write a function that takes a string as input and returns the string reversed.

Input: "hello"
Output: "olleh"
'''
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # lst = []
        # for i in s:
        #     lst.append(i)
        # lst.reverse()
        # return ''.join(lst)
        return  s[::-1]