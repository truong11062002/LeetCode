
def remove_element(nums, val):
    
    
    nums = [x for x in nums if x != val]
    return nums

if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    print(remove_element(nums, val)) # 2

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(remove_element(nums, val)) # 5