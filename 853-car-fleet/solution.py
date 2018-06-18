class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        time = [(target - pos) / float(vel) for pos, vel in reversed(sorted(zip(position, speed)))]
        prev, fleet = 0, 0
        for cur in time:
            if cur > prev:
                prev = cur
                fleet += 1
        return fleet