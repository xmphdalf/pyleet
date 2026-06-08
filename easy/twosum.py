"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]

Example 2:
  Input: nums = [3,2,4], target = 6
  Output: [1,2]

Example 3:
  Input: nums = [3,3], target = 6
  Output: [0,1]

Constraints:
  2 <= nums.length <= 10^4
  -10^9 <= nums[i] <= 10^9
  -10^9 <= target <= 10^9
  Only one valid answer exists.
"""

def two_sum(nums: list[int], target: int) -> list[int]:
  seen = {}
  for i, num in enumerate(nums):
    needed = target - num
    if needed in seen:
      return [seen[needed], i]
    seen[num] = i
  return []

print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))
print(two_sum([-1,-2,-3,-4,-5], -8))
print(two_sum([-1,-2,-3,-4,-5], -8))