from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans_dict = defaultdict(list)
        for w in strs :
            ans_dict[''.join(sorted(w))].append(w)
        return ans_dict.values()
        