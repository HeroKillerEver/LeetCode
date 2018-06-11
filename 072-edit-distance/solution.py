class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        """
        recursive solution with memorization: AC
        """
        self.memo = {}
        return self.minimum(word1, word2)
    
    def minimum(self,  word1, word2):
        if (word1, word2) in self.memo: return self.memo[(word1, word2)]
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[-1] != word2[-1]:
            self.memo[(word1, word2)] = min(self.minimum(word1[:-1], word2) + 1, # delete word1[-1]
                      self.minimum(word1, word2[:-1]) + 1,  # insert word2[-1] into word1[-1]
                      self.minimum(word1[:-1], word2[:-1]) + 1) # replace word1[-1] to word2[-1]
        else:
            self.memo[(word1, word2)] = self.minimum(word1[:-1], word2[:-1])
        return self.memo[(word1, word2)]
