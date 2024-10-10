arr = [10, 4, 8, 13, 20]
x = 8
y = 1
res = 0
arr.sort(reverse=True)
while arr[0] > 0:
    arr[0] -= x
    maintained = False
    for i in range(1, len(arr)):
        arr[i] -= y
        if not maintained and arr[i-1] <= arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
        else:
            maintained = True
    res += 1

print(res)