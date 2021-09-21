a = []
flag1 = True
flag2 = "д"
p = 0
print("Вводите числа, если захотите закончить, то введите 'з'")
while flag2 == "д":
    while flag1:
        coor = input()
        if coor == "з":
            flag1 = False
        else:
            a.append(int(coor))
    for i in range(len(a)):
        x = a[i]
        for j in range(i + 1, len(a)):
            y = a[j]
            for k in range(j+1, len(a)):
                z = a[k]
                if (x + y > z) and (x + z > y) and (y + z > x):
                    if x + y + z > p:
                        p = x + y + z
    print(p)
    flag2 = input("Хотите продолжить? д/н: ")