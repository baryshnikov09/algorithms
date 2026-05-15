def find_peak_index(A):
    left = 0
    right = len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] < A[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left + 1

A = list(map(int, input().split()))
p = find_peak_index(A)

print(p)