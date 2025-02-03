def fib(n):
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

fib(2000)
print(fib(2000))
print(fib2(2000))

print(ask_ok('Do you really want to quit?'))
print(ask_ok('OK to overwrite the file?', 2))
print(ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!'))

i = 5
def f(arg=i):
    print(arg)

i = 6
f()

def f2(a, L=[]):
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))

def f3(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f3(1))
print(f3(2))
print(f3(3))

# arguments will be those passed in after kind
# keywords will be all passed in as name=value
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="Joohn Cleese",
           sketch="Cheese Shop Sketch")

cheeseshop("Limburger", 
           shopkeeper="Michael Palin",
           client="Joohn Cleese",
           sketch="Cheese Shop Sketch")

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2)
standard_arg(arg=2)
pos_only_arg(2)
kwd_only_arg(arg=3)
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)

