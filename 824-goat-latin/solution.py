class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = ['a', 'e', 'i', 'o', 'u']
        sentence = S.split()
        res = []
        for idx, word in enumerate(sentence):
            if word[0].lower() in vowel:
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            word += 'a' * (idx + 1)
            res.append(word)
        return ' '.join(res)