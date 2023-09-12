def fibCalc(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = (fib[i - 1] % 10 + fib[i - 2] % 10) % 10
    return fib[n]

n = int(input())
print(fibCalc(n))