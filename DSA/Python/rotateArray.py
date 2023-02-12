def rotateArray(arr, d, n):
    k = arr.index(d)

    temp = []
    temp = arr[k+1:] + arr[:k+1]
    return temp

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    d = 2
    N = len(arr)

    # Function rotate array
    arr = rotateArray(arr, d, N)
    for i in arr:
        print(i, end=" ")

