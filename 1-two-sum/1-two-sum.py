class Solution:
    def twoSum(self, nums, target) :
        dict_num = {}
        for i in range(len(nums)) :
            dict_num[nums[i]] = i
        for x in range(len(nums)) :
            a = target - nums[x]
            if a in dict_num :
                if x != dict_num[a] :
                    return [x, dict_num[a]]