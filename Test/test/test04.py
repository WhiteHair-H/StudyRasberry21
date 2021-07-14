m = 0
n = 1

def func():
    global m
    global n
    m = m + 1
    n += 1

func()
print(m, n)


def counter(max):
    t = 0

    def output(): # counter함수에 속하는 함수로, 따로 호출 불가
        print('t = {0}'.format(t))
    

    while t < max:
        output()
        t += 1


counter(10)
# output()

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(10))
print(factorial(9))
print(factorial(8))
print(factorial(7))
print(factorial(6))
print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))


# lambda
a = lambda x, y : x * y
print(a(2, 8))


# Closure

def calc(a):
    def add(b):
        return a + b
    return add

sum = calc(1)
print(sum(2))

