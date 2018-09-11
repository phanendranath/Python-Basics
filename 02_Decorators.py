#!/usr/bin/python

def outer(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            return e
        else:
            return func(*args, **kwargs)

    return inner


@outer                    # comment this line and observe difference
def div(a, b):
    return a / b

print div(4, 2)
print div(4, 0)



@outer
def add(a, b):
    return a + b



print add(2, 3)
print add('a', 3)
