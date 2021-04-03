def fib(n: int, m: int = 1, f0: int = 1, f1: int = 1):
    if n == 0 or n == 1:
        return f1
    if m == n:
        return f1
    f0, f1 = f1, f0 + f1
    m += 1
    return fib(n, m, f0, f1)


def solution():
    n = int(input().strip())
    c = fib(n)
    print(c)


if __name__ == '__main__':
    solution()