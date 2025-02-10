class Solution:
    def helper(self, nums: List[int], low: int, high: int):
        if low > high:
            return -1
        
        mid = (low + high) // 2
        if nums[mid] < target:
            return self.helper(nums, mid + 1, high)
        elif target < nums[mid]:
            return self.helper(nums, low, mid - 1)
        else:
            return mid

    def search(self, nums: List[int], target: int) -> bool:
        return self.helper(nums, low, high)