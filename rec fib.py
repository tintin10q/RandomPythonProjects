def trace(fun):
    """Recursion function trace function that displays recursion levels."""
    trace.level = 0

    def wrapper_func(n):
        """Wrapper function of the trace decorator"""
        print('|   ' * trace.level + '|--', fun.__name__, n)
        trace.level += 1
        output = fun(n)
        print('|   ' * trace.level + '|-- return', output)
        trace.level -= 1
        return output

    return wrapper_func


@trace
def fib(n):
    """Returns the nth fibonacci number."""
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(3))


@trace
def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


print(factorial(4))
