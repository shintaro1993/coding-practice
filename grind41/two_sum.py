"""Step2
変数名を改善する

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            other_num = target - i
            if other_num in num_to_dict:
                return [i, num_to_index[other_num]]
            num_to_index[num] = i
        return None