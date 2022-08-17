class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit_dict = {}
        re_digits = []
        for d in digits :
            check = digit_dict.get(d)
            if check == None :
                digit_dict[d] = 1
                re_digits.append(d)
            elif check < 3 :
                digit_dict[d] += 1
                re_digits.append(d)
        
        ans = set()
        first = [i for i, v in enumerate(re_digits) if v != 0]
        second = list(range(len(re_digits)))
        third = [i for i, v in enumerate(re_digits) if v % 2 == 0]
        for x in first :
            for y in second :
                for z in third :
                    if (x != y) and (y != z) and (z != x) :
                        ans.add((re_digits[x] * 100) + (re_digits[y] * 10) + re_digits[z])
        ans = list(ans)
        ans.sort()
        return ans