def foo(n):
    if n == 0:
        return
    foo(n-1)
    return

foo(4)