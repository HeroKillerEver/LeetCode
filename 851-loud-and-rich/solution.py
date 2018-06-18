from collections import defaultdict
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        self.graph = defaultdict(list)
        for u, v in richer:
            self.graph[v].append(u)
        self.quiet = quiet
        self.seen = {}
        return [self.minimum(i)[1] for i in range(len(quiet))]
            
    
    def minimum(self, node):
        
        if node in self.seen: return self.seen[node]
        res = (self.quiet[node], node)
        if node in self.graph:
            for child in self.graph[node]:
                res = min(res, self.minimum(child))
        self.seen[node] = res
        return res