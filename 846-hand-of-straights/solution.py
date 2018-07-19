class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        length = len(hand)
        if length % W: return False
        K = length / W
        hand.sort()
        while K:
            tmp = []
            handcp = hand[:]
            for idx, card in enumerate(handcp):
                if len(tmp) < W:
                    if not tmp or card == tmp[-1] + 1:
                        tmp.append(card)
                        hand.remove(card)
                else: break
            if len(tmp) < W: return False
            K -= 1
        return not hand

#####################################
from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        hand = Counter(hand)
        
        while hand:
            start = min(hand)
            for card in xrange(start, start+W):
                if not hand[card]: 
                    return False
                elif hand[card] == 1:
                    del hand[card]
                else:
                    hand[card] -= 1
        return True