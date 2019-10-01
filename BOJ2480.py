arr = list(map(int, input().split()))

if arr.count(arr[0]) == 3:
    print(10000 + arr[0] * 1000)
elif arr.count(arr[0]) == 2 :
    print(1000 + arr[0] * 100)
elif arr.count(arr[1]) == 2:
    print(1000 + arr[1] * 100)
else:
    print(max(arr) * 100)