def GCD(a, b):
    if a == 0:
        return b
    return GCD(b % a, a)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(GCD(a, b))
