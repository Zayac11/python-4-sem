from math import sqrt, e, tan, log, sin, cos, fabs, pow


# Вариант 12

def f13(n, m):
    sum_1, sum_2 = 0, 0
    for i in range(n + 1):
        if i == 0:
            continue
        for j in range(m + 1):
            if j == 0:
                continue
            sum_1 += 19*pow(j, 2) + 3*pow(i, 5)
            sum_2 += pow(i, 3) - pow(j, 6)
    result = 57 * sum_1 + 36 * sum_2
    return result


print('\nTASK #3')
n, m = 37, 48
print(f'Test #1: func({n}, {m}) = {f13(n, m)}')
n, m = 28, 43
print(f'Test #2: func({n}, {m}) = {f13(n, m)}')


def f21(x: list) -> int:
    if x[2] == "stan":
        if x[1] == 1973:
            if x[3] == 'diff':
                return 0
            elif x[3] == 'scss':
                return 1
            elif x[3] == 'ini':
                return 2
        elif x[1] == 1983:
            return 3
        elif x[1] == 1969:
            if x[0] == 2013:
                if x[1] == 2012:
                    return 4
                elif x[1] == 1982:
                    return 5

    elif x[2] == 'self':
        if x[3] == "diff":
            return 6
        elif x[3] == "scss":
            return 7
        elif x[3] == "ini":
            return 8

    elif x[2] == 'abap':
        if x[1] == 1973:
            if x[3] == 'diff':
                return 9
            elif x[3] == 'scss':
                return 10
            elif x[3] == 'ini':
                return 11
        elif x[1] == 1981:
            return 12
        elif x[1] == 1969:
            return 13


print(f21([1982, 1969, 'abap', 'diff']))
print(f21([1982, 1981, 'self', 'ini']))