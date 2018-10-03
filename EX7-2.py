m = float(input("Variable M:"))
n = float(input("Variable N:"))
while m > 0:
    n,m = m, n%m
    print("N: ", n, "-", "M: ", m)
