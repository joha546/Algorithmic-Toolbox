def Periodic(m):
    a, b = 0, 1
    c = a + b
    for i in range(m * m):
        c = (a + b) % m
        a = b
        b = c
        if a == 0 and b == 1:
            return i + 1

def Solve(n, m):
    remainder = n % Periodic(m)
    first = 0
    second = 1
    res = remainder
    for i in range(1, remainder):
        res = (first + second) % m
        first = second
        second = res
    return res % m

if __name__ == "__main__":
    n = int(input())
    print((Solve(n + 1, 10) * Solve(n, 10)) % 10)
