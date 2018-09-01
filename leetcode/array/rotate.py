'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

eg:
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
'''

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        ma3 = []
        ma2=[ i for row in matrix  for i in row]
        temp = []
        len1 = len(ma2)
        len2 = len(matrix)
        len3 = len(matrix[0])
        for i in range(len1//len2):
            temp = ma2[i-len3::-len3]
            ma3.append(temp)
            temp = []
        matrix[:]=ma3