class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        l = ["!", "?", "'", ",", ";", "."]
        for d in l :
            paragraph = paragraph.replace(d, ' ')
        w_list = paragraph.split()
                    
        ans_dict = {}
        for w in w_list :
            check = ans_dict.get(w)
            if check == None :
                ans_dict[w] = 1
            else :
                ans_dict[w] += 1
        
        [ans_dict.pop(key, None) for key in banned]
        
        return sorted(ans_dict.items(), key = lambda item: item[1])[-1][0]