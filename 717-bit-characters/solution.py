from collections import deque
class Solution(object):
    def isOneBitCharacter_1(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        """
        time complexity: O(n^2)
        space complexity: O(n)
        """
        while len(bits) > 1:
            if bits[0]:
                bits = bits[2:]
            else:
                bits = bits[1:]
        return bits == [0]

class Solution(object):
    def isOneBitCharacter_1(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        """
        using queue
        time complexity: O(n)
        space complexity: O(n)
        """
        bits_queue = deque(bits)
        while len(bits_queue) > 1:
            if bits_queue[0]:
                bits_queue.popleft()
                bits_queue.popleft()
            else:
                bits_queue.popleft()
        return bits_queue == deque([0])


class Solution(object):
    def isOneBitCharacter_3(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """        
        length = 0
        while length < len(bits) - 1:
            if bits[length]:
                length += 2
            else:
                length += 1
        return length == len(bits) - 1