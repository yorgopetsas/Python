stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())


{'__module__': '__main__', 'varia': 1, '__init__': <function ExampleClass.__init__ at 0x7f6b0e3940e0>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}

{'__module__': '__main__', 'varia': 2, '__init__': <function ExampleClass.__init__ at 0x7f6b0e3940e0>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
{}