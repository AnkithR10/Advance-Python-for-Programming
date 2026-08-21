def add(n):
    if n == 0:
        return 0
    else:
        return n + add(n-1)

n = int(input("Enter N:"))
print("sum of",n,"number is",add(n))
