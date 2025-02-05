# Fibonacci numbers module

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def fib3(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    import sys
    for number in fib3(int(sys.argv[1])):
        print(number)

