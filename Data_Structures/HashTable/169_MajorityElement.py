def majorityElement(nums: List[int]) -> int:
    # Dictionary to store the count of each element
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    # Find the element with the maximum count
    return max(count, key=count.get)