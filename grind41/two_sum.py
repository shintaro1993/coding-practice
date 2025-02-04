"""Step1


"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(nums):
            other_num = target - num
            if other_num in seen:
                return [i, seen[other_num]]
            seen[num] = i
        return None