def nFib_operation(n: int) -> int:
    old = 0
    crt = 1
    result = 1
    for i in range(n):
        result = old + crt
        old = crt
        crt = result
    return result
