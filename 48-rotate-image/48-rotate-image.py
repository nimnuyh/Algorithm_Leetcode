class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        clone = matrix[:]
        for i in range(len(clone[0])) :
            line = []
            for l in clone :
                line.append(l[i])
            line.reverse()
            matrix[i] = line