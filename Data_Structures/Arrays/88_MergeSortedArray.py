def mergeSortedArray(nums1, m, nums2, n):
    
    for i in range(len(nums1)):
        if nums1[i] == 0:
            if nums2 != []:
                nums1[i] = nums2.pop(0)
            else:
                break
            
    return nums1.sort()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(mergeSortedArray(nums1, m, nums2, n))