class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0 for i in range(len(temperatures))]
        stack = [[-1, temperatures[0]]]
        temperatures.pop(0)
        for i, tmp in enumerate(temperatures) :
            while stack and stack[-1][1] < tmp :
                last_idx, last_tmp = stack.pop()
                ans[last_idx + 1] = i - last_idx
            else :
                stack.append([i, tmp])
        return ans