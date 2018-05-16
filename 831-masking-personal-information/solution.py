class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if '@' in S:
            name, domain = S.split('@')
            return name[0].lower() + '*'*5 + name[-1].lower() + '@' + domain.lower()
        else:
            digits = ''.join([item for item in S if item.isdigit()])
            if len(digits) == 10:
                return '***-***-{}'.format(digits[-4:])
            else:
                return "+{}-".format('*' * (len(digits) - 10)) + '***-***-{}'.format(digits[-4:])