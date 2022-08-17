class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        j = list(jewels)
        s = list(stones)
        return len([x for x in s if x in j])