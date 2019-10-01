arr = []
sum = 0

for i in range(0, 5, 1):
    arr.append(int(input()))
    sum += arr[i]

arr.sort()

mid = arr[2]
sum /= 5

print(int(sum))
print(mid)