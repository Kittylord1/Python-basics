from time import time

def perfomance(fn):
    def wrapper(*args,**kwargs):
        t1 = time()
        result = fn(*args,**kwargs)
        t2 = time()
        print(f'took {t2-t1}time to complete')
        return result
    return wrapper

@perfomance
def long_time():
    for i in range(100000000):
        i*2


long_time()




def my_decorator(func):
    def wrap():
        print('*******')
        func()
        print('*******')
    return wrap


def abc():
    print('hi there')


a = my_decorator(abc)

a()

@my_decorator
def acd():
    print('hello')

acd()

def my_decorator1(func):
    def wrap(*args,**kwargs):
        print('*******')
        func(*args,**kwargs)
        print('*******')
    return wrap

@my_decorator1
def hi(greeting,emoji=':('):
    print(greeting,emoji)

hi('hiiii')

