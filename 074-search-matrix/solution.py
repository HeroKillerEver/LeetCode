class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        if not matrix[0]: return False
        m = len(matrix)
        n = len(matrix[0])
        low_m, high_m = 0, m
        while low_m < high_m - 1:
            tmp = (low_m + high_m) // 2
            if matrix[tmp][0] < target:  low_m = tmp
            elif matrix[tmp][0] > target: high_m = tmp
            else: return True
        low_c, high_c = 0, n
        flag_m = low_m
        while low_c < high_c - 1:
            tmp = (low_c + high_c) // 2
            if matrix[flag_m][tmp] < target:  low_c = tmp
            elif matrix[flag_m][tmp] > target: high_c = tmp
            else: return True
        flag_c = low_c
        return matrix[flag_m][flag_c] == target
        