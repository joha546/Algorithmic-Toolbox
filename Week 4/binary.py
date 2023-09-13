def binary_search(a, left, right, x):
    if left < 0 or right >= len(a) or left > right:
        return -1
    mid = left + (right - left) // 2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary_search(a, left, mid - 1, x)
    else:
        return binary_search(a, mid + 1, right, x)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for i in range(m):
    print(binary_search(a, 0, len(a) - 1, b[i]), end=' ')
