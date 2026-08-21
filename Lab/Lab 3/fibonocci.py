def recursive_fib(n):
    if n == 0:
        return 0
    elif n== 1:
        return 1
    else:
        return recursive_fib(n-1)+recursive_fib(n-2)

n = int(input("Enter the Number of Temrs:"))
for i in range(n+1):
    print(recursive_fib(i),end=" ")
4