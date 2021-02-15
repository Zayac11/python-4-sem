from math import sqrt, e, tan, log, sin, cos, fabs, pow
# Вариант 12

def f11(x, y, z):
    result = pow((fabs(x) + log(y) + 82), 6) - tan(z) + tan(84 * pow(z, 5) - pow(x, 7)/41) \
             + fabs(y) - 24 - (pow(x, 7) + pow(z, 3))
    return result


# print('\nTASK #1')
# x = -5
# y = 22
# z = -30
# print(f'Test #1: func({x}, {y}, {z})={f11(x,y,z)}')
#
# x = -28
# y = 54
# z = 90
# print(f'Test #2: func({x}, {y}, {z})={f11(x,y,z)}')


def f12(x):
    if x < -61:
        result = pow(e, (fabs(x) + log(x) + 82)) + tan(87 * pow(x, 8))
    elif -61 <= x < -50:
        result = x*x + tan(x)
    elif -50 <= x < -5:
        result = 44 * pow(x, 8) + 43 * pow(x, 5) - 58
    elif -5 <= x < 50:
        result = pow((pow(x, 5) - pow(x, 7)/99), 3) + 23 * pow(x, 4)
    else:
        result = 65 * pow(x, 7) + 34 * pow(x, 4) - 85
    return result
    # else:
    #     return 'condition is wrong'

# print('\nTASK #2')
# x = -31
# print(f'Test #1: func({x})={f12(x)}')
# x = 92
# print(f'Test #2: func({x})={f12(x)}')


def f13(n, m):
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


# print('\nTASK #3')
# n, m = 79, 50
# print(f'Test #1: func({n}, {m})={f13(n, m)}')
# n, m = 33, 21
# print(f'Test #2: func({n}, {m})={f13(n, m)}')


def f14(n):
    if n == 0:
        return 10
    if n == 1:
        return 8
    result = cos(f14(n - 1)) - fabs(f14(n - 2))
    return result


# print('\nTASK #4')
# n = 16
# print(f'Test #1: func({n})={f14(n)}')
# n = 5
# print(f'Test #2: func({n})={f14(n)}')
