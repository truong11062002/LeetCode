# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n

        while start <= end:
            mid = start + (end - start) // 2
            if end == start:
                return end

            if isBadVersion(mid) == False:
                start = mid + 1
            else:
                end = mid
        return end

        