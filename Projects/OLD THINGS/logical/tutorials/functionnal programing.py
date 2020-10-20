def do_twice (func, arg) :
    return func(func(arg))


def add_ten (x):
    return x + 1

print (do_twice(add_ten, 2))