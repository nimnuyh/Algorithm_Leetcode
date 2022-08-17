class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I' : 1, 
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        roman = list(s)
        ans = 0
        for r in range(len(roman)) :
            if r == len(roman) - 1:
                ans += roman_dict[roman[r]]
            else :
                if roman_dict[roman[r]] < roman_dict[roman[r + 1]] :
                    ans -= roman_dict[roman[r]]
                else :
                    ans += roman_dict[roman[r]]
        return ans