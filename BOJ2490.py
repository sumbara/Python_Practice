for _ in range(3):
    arr = list(map(int, input().split()))
    cnt = sum(arr)
    if cnt == 0:
        print("D")
    elif cnt == 1:
        print("C")
    elif cnt == 2:
        print("B")
    elif cnt == 3:
        print("A")
    elif cnt == 4:
        print("E")