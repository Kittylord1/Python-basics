def generetor_func(num):
    for i in range(num):
        yield i * 2

a =  generetor_func(10)
next(a)
next(a)
print(next(a))
print(next(a))