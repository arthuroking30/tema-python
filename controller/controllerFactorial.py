def factorial_operation(n: int) -> int:
    res = n
    while n > 1:
        res = res * (n - 1)
        n -= 1
    return res
