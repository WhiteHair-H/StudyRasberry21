m = 0 
n = 1

def func():
    global m , n # 전역 변수 선언
    m += 1
    n += 1

func()
print(m, n)


def counter(max):
    t = 0

    def output(): # counter안에 있는 함수는 따로 사용불가
        print('t = {0}'.format(t))

    while t < max :
        output()
        t += 1

counter(10)
# output 호출불가

# 재귀함수 - 기하급수적으로 변화함
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n -1)

print(factorial(10))
print(factorial(7))
print(factorial(3))
print(factorial(2))

# lambda = 익명함수
a = lambda x , y : x * y
print(a(2,5))

# Closure

def calc(a):
    def add(b):
        return a + b
    return add

sum = calc(1)
print(sum(2))



