def TwoSum(nums, target):
    # Create a dictionary to store the values
    hashMap = {}
    
    # Loop through the list
    for i, v in enumerate(nums):
        diff = target - v
        # Check if the value is in the dictionary
        if diff in hashMap:
            # If it is, return the index of the value and the current index
            return [hashMap[diff], i]
        hashMap[v] = i
    
    return 