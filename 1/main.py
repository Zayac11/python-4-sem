from math import sqrt, e, tan, log, sin, cos, fabs, pow
# Вариант 12

def func_1(x, y, z):
    result = pow(x, 2) + fabs(y) + ((pow(x, 3) - y)/(74*x - log(z) + 18)) \
             + ((93*pow(x, 6) - pow(x, 3))/(pow(x, 8)/56 - pow(x, 7)))
    return result


print('\nTASK #1')
x = -63
y = -48
z = 73
print(f'Test #1: func({x}, {y}, {z})={func_1(x,y,z)}')

x = -50
y = 39
z = 86
print(f'Test #2: func({x}, {y}, {z})={func_1(x,y,z)}')


def func_2(x):
    if x < -10:
        result = 24 * (28*pow(x, 8) + tan(x) + pow(x, 3))
    elif -10 <= x < 1:
        result = 74 * x - log(x) + 18
    elif 1 <= x < 11:
        result = 25 * pow((63 * pow(x, 2) + 30 * pow(x, 4)), 2) + cos(x)
    elif 11 <= x < 35:
        result = pow((log(x) - 57 * pow(x, 7) + 89), 2) - pow(e, x)
    elif x >= 35:
        result = pow(x, 2) + fabs(x)
    else:
        return 'condition is wrong'
    return result

print('\nTASK #2')
x = 72
print(f'Test #1: func({x})={func_2(x)}')
x = 64
print(f'Test #2: func({x})={func_2(x)}')


def func_3(n, m):
    sum_1, sum_2 = 0, 0
    for i in range(n + 1):
        if i == 0:
            continue
        for j in range(m + 1):
            if j == 0:
                continue
            sum_1 += tan(j) - pow(j, 3)
            sum_2 += pow(i, 5) - pow(i, 2)
    result = 80 * sum_1 + 18 * sum_2
    return result


print('\nTASK #3')
n, m = 79, 50
print(f'Test #1: func({n}, {m})={func_3(n, m)}')
n, m = 33, 21
print(f'Test #2: func({n}, {m})={func_3(n, m)}')


def func_4(n):
    if n == 0:
        return 10
    if n == 1:
        return 8
    result = cos(func_4(n-1)) - fabs(func_4(n-2))
    return result


print('\nTASK #4')
n = 16
print(f'Test #1: func({n})={func_4(n)}')
n = 5
print(f'Test #2: func({n})={func_4(n)}')
