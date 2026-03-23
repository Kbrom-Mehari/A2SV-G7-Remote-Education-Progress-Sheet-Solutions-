m, n = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
i = 0
result = []
for num in arr2:
    while i < m and arr1[i] < num:
        i += 1
    result.append(i)
print(' '.join(map(str, result)))