def searchInsert(nums, target):
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            start = mid + 1
        else: 
            end = mid -1
    return end + 1

nums = [1, 3, 5, 6]
target = 2

print(searchInsert(nums, target))

