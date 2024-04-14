from typing import List


def singleNumber(nums: List[int]) -> int:
    uni_nums = set(nums)
    appears = {}
    for num in uni_nums:
        if nums.count(num) == 1:
            return num


nums = [1]

print(singleNumber(nums))
