def mySqrt(x):
    start = 0
    end = x
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if mid * mid == x:
            return mid
        if mid * mid < x:
            start = mid + 1
        else:
            end = mid - 1
    return end

x = 8
print(mySqrt(x))

