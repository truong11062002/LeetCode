def reverseArray(arr, start, end):
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

A = [1,2,3,4,5,6]
print(A)

reverseArray(A, 0, 5)
print("List sau khi reverse")
print(A)
