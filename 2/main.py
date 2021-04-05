
def f21(x: list) -> int:
    if x[3] == "ocaml":
        if x[4] == 2015:
            if x[2] == 2013:
                return 0
            elif x[2] == 2006:
                if x[0] == 2009:
                    return 1
                elif x[0] == 1996:
                    return 2
                elif x[0] == 2007:
                    return 3
        elif x[4] == 2010:
            if x[2] == 2013:
                if x[1] == "genie":
                    return 4
                elif x[1] == "yang":
                    return 5
            elif x[2] == 2006:
                return 6
    elif x[3] == 'ini':
        if x[1] == "genie":
            return 7
        elif x[1] == "yang":
            return 8
    elif x[3] == 'xtend':
        return 9


# print(f21([2009, 'yang', 2006, 'xtend', 2010]))
# print(f21([2007, 'yang', 2013, 'ini', 2010]))
# print()


def get_bit(n, i):
    return n & (1 << i) == (1 << i)


def f22(n):
    b = 0
    # a
    for i in range(2):
        b = b | get_bit(n, (i + 0)) << (i + 18)
    # b
    for i in range(12):
        b = b | get_bit(n, (i + 2)) << (i + 20)
    # c
    for i in range(6):
        b = b | get_bit(n, (i + 14)) << (i + 1)
    # d
    for i in range(2):
        b = b | get_bit(n, (i + 20)) << (i + 16)
    # e
    for i in range(5):
        b = b | get_bit(n, (i + 22)) << (i + 10)
    # f
    for i in range(2):
        b = b | get_bit(n, (i + 26)) << (i + 14)
    # g
    for i in range(3):
        b = b | get_bit(n, (i + 28)) << (i + 7)
    # h
    for i in range(1):
        b = b | get_bit(n, (i + 31)) << (i + 0)

    return int(b)
#
#
# print(hex(f22(0x25ec6c03)))
# print(hex(f22(0x8abc9d07)))
# print()


def delete_none_string(table):
    must_delete = set()
    for i, string in enumerate(table):
        if all(x is None for x in table[i]):
            must_delete.add(i)

    k = 0
    for i in must_delete:
        table.pop(i - k)
        k += 1


def delete_duplicated_strings(table):
    must_delete = set()
    for i, string in enumerate(table):
        for j, temp_string in enumerate(table):
            if i < j and string == temp_string:
                must_delete.add(j)

    k = 0
    for i in must_delete:
        table.pop(i - k)
        k += 1


def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def f23(table: list):
    # Удаляем массивы с None
    delete_none_string(table)
    # print(table)

    # Удалим дубликаты среди строк
    delete_duplicated_strings(table)

    # Транспонируем матрицу
    table = [list(i) for i in zip(*table)]

    # Удалим строки, которые на самом деле являются столбцами
    delete_duplicated_strings(table)

    # Транспонируем матрицу обратно
    table = [list(i) for i in zip(*table)]

    # Преобразуем элементы матрицы
    for i, string in enumerate(table):
        for j, el in enumerate(string):
            temp_el = el.split('@', 1)[0]
            if temp_el == 'да':
                temp_el = 'true'
            elif temp_el == 'нет':
                temp_el = 'false'
            if is_digit(temp_el):
                temp_el = "{:.0%}".format(float(temp_el))
                # print(temp_el)
            table[i][j] = temp_el

    # Выведем конечную матрицу
    # for el in table:
    #     print(el)
    # print()

    return table

# table_1 = [
#     ['ticagak42@yahoo.com', 'нет', '0.1', 'нет'],
#     [None, None, None, None],
#     ['mafomanz10@gmail.com ', 'да', '0.1', 'да'],
#     [None, None, None, None],
#     ['sodunli69@gmail.com', 'нет', '0.9', 'нет'],
# ]
#
# table_2 = [
#     [None, None, None, None],
#     ['datakan98@yahoo.com', 'да', '0.2', 'да'],
#     ['muzosman33@rambler.ru ', 'нет', '0.1', 'нет'],
#     [None, None, None, None],
#     ['kenucman21@yandex.ru', 'нет', '0.8', 'нет'],
# ]

# f23(table_1)
# f23(table_2)