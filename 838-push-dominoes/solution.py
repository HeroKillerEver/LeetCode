class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        N = len(dominoes)
        force = [0] * N
        tmp_force = 0
        for idx, domino in enumerate(dominoes):
            if domino == 'R':
                tmp_force = len(dominoes)
                force[idx] += tmp_force
            elif domino == '.':
                tmp_force = tmp_force - 1 if tmp_force else 0
                force[idx] += tmp_force if tmp_force else 0
            else:
                tmp_force = 0
        tmp_force = 0
        for idx, domino in enumerate(reversed(dominoes)):
            if domino == 'L':
                tmp_force = len(dominoes)
                force[N - 1 - idx] -= tmp_force
            elif domino == '.':
                tmp_force = tmp_force - 1 if tmp_force else 0
                force[N - 1 - idx] -= tmp_force if tmp_force else 0
            else:
                tmp_force = 0
        return ''.join(map(lambda x: 'L' if x < 0 else 'R' if x > 0 else '.', force))