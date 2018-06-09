class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        all_set = set(range(len(rooms)))
        queue = [rooms[0]]
        res = set()
        res.add(0)
        while queue:
            keys = queue.pop(0)
            if keys:
                for key in keys:
                    if not key in res:
                        res.add(key)
                        queue.append(rooms[key])
        return res == all_set