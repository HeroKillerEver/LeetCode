class Solution(object):
    def majorityElement_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            dic.setdefault(num, 0)
            dic[num] += 1
        return max(dic.keys(), key=dic.get)

class Solution(object):        
    def majorityElement_2(self, nums):
        """
        two liner Pythonic solution
        """
        dic = collections.Counter(nums)
        return max(dic.keys(), key=dic.get)

class Solution(object):
    def majorityElement_3(self, nums):
        """
        using stack
        """
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
            else:
                if stack[-1] != num:
                    stack.pop()   
                else:
                    stack.append(num)
        return stack[-1]

class Solution(object):
    def majorityElement_4(self, nums):
        """
        Boyer-Moore Voting Algorithm
        time complexity: O(n)
        space complexity: O(1)
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


        
