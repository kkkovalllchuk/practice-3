def fact(n):
    if n == 1:
        return 1
    else:
        k = n * fact(n - 1)
        return k