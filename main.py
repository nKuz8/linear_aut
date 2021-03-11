q = {"0": 2,
     "1": [1, 1],
     "2": [1, 1, 1],
     "3": [1, 0, 1, 1],
     "4": [1, 0, 0, 1, 1],
     "5": [1, 0, 0, 1, 0, 1],
     "6": [1, 0, 0, 0, 0, 1, 1],
     "7": [1, 0, 0, 0, 0, 0, 1, 1],
     "8": [1, 0, 0, 0, 1, 1, 0, 1, 1],
     "10": [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1],
     "12": [1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1]}


def matrix_mult(matrix_1, matrix_2):
    if matrix_check(matrix_1, matrix_2, "mult"):
        return 0
    else:
        result_matrix = []
        result_row = []
        resul_mult = [0] * len(mod)

        for i in range(0, len(matrix_1)):
            for j in range(0, len(matrix_2[0])):
                for k in range(0, len(matrix_1[0])):
                    resul_mult = add_mod(mult_mod(matrix_1[i][k], matrix_2[k][j]), resul_mult, carry=True)
                result_row.append(resul_mult)
                resul_mult = [0] * len(mod)
            result_matrix.append(result_row)
            result_row = []

        return result_matrix


def matrix_check(matrix_1, matrix_2, operation):
    return False
    # if operation == "mult":
    #     return len(matrix_1[0]) != len(matrix_2)
    # elif operation == "sum":
    #     return len(matrix_1) != len(matrix_2) and len(matrix_1[0]) != len(matrix_2[0])


def matrix_add(matrix_1, matrix_2):
    if matrix_check(matrix_1, matrix_2, "sum"):
        return 0
    else:
        result_matrix = []
        result_row = []
        for i in range(0, len(matrix_1)):
            for j in range(0, len(matrix_1[0])):
                result_row.append(add_mod(matrix_1[i][j], matrix_2[i][j], carry=True))
            result_matrix.append(result_row)
            result_row = []

        return result_matrix


def matrix_print(matrix):
    for row in matrix:
        for el in row:
            print("{} ".format(el), end="")
        print()
    print("\n")


def add_mod(op1, op2, carry=False, div=False):
    if type(op1) is int and type(op2) is int:
        return (op1 + op2) % 2
    else:
        overflow = 0
        result = []

        while len(op1) < len(op2):
            op1.insert(0, 0)
        while len(op2) < len(op1):
            op2.insert(0, 0)
        for i in range(len(op1) - 1, -1, -1):
            if (op1[i] != op2[i]) != overflow:
                result.append(1)
            else:
                result.append(0)

            if carry:
                if op1[i] + op2[i] + overflow > 1:
                    overflow = 1
                else:
                    overflow = 0

        if overflow == 1:
            result.append(overflow)

        result.reverse()

        if div:
            return result
        else:
            return div_mod(result, mod)


def div_mod(op1, mod):
    if mod == 0:
        return op1 % 2
    else:
        mod_oper = mod.copy()
        while op1[0] == 0 and len(op1) > len(mod):
            op1.pop(0)

        while (op1[0:-len(mod) + 1] != [0] * (len(op1) - len(mod) + 1) and len(op1) > len(mod)) or (len(op1) == len(mod) and op1[0] == 1 and op1 != mod):
            while len(mod_oper) < len(op1):
                mod_oper.append(0)

            op1 = add_mod(op1, mod_oper, div=True)
            while op1[0] == 0:
                op1.pop(0)
                if len(op1) <= 0:
                    break

            mod_oper = mod.copy()

        while op1[0] == 0 and len(op1) > len(mod):
            op1.pop(0)

        while len(op1) < len(mod):
            op1.insert(0, 0)

        while len(op1) > len(mod):
            op1.pop(0)

        return op1


def mult_mod(op1, op2):
    if type(op1) is int and type(op2) is int:
        return (op1 * op2) % 2
    else:
        factor = op1.copy()
        result = [0] * len(op2)

        for i in range(len(op2) - 1, -1, -1):
            if op2[i] == 1:
                for j in range(len(op2) - 1 - i, 0, -1):
                    factor.append(0)
                while len(result) < len(factor):
                    result.insert(0, 0)

                result = add_mod(result, factor)
                factor = op1.copy()

        return div_mod(result, mod)


def fun(s, matrix_A, x, matrix_B):
    return matrix_add(matrix_mult(s, matrix_A), matrix_mult(x, matrix_B))


def main():
    global mod
    read_flags = [False] * 4
    A = []
    B = []
    C = []
    D = []
    polinome = []
    matrix_row = []

    with open("params.txt", 'r') as file:
        for line in file:
            if line[0] == "q":
                mod = q[line[line.find("^") + 1]]
            elif line == "matrix_A\n":
                read_flags[0] = True
                continue
                print("1")
            elif line == "matrix_B\n":
                read_flags[1] = True
                continue
            elif line == "matrix_C\n":
                read_flags[2] = True
                continue
            elif line == "matrix_D\n":
                read_flags[3] = True
                continue
            elif line == "end\n":
                read_flags = [False] * 4
                continue

            if read_flags[0]:
                for polies in line.split(" "):
                    polinome = list(map(lambda x: int(x), list(polies.replace("\n", ""))))
                    matrix_row.append(polinome)
                A.append(matrix_row)
                matrix_row = []
            elif read_flags[1]:
                for polies in line.split(" "):
                    polinome = list(map(lambda x: int(x), list(polies.replace("\n", ""))))
                    matrix_row.append(polinome)
                B.append(matrix_row)
                matrix_row = []
            elif read_flags[2]:
                for polies in line.split(" "):
                    polinome = list(map(lambda x: int(x), list(polies.replace("\n", ""))))
                    matrix_row.append(polinome)
                C.append(matrix_row)
                matrix_row = []
            elif read_flags[3]:
                for polies in line.split(" "):
                    polinome = list(map(lambda x: int(x), list(polies.replace("\n", ""))))
                    matrix_row.append(polinome)
                D.append(matrix_row)
                matrix_row = []

    raw_s = input("Enter s0: ")
    s = []
    if mod == 2:
        s.append(list(map(lambda x: int(x), raw_s.split(" "))))
    else:
        s_row = []
        for polies in raw_s.split(" "):
            polinome = list(map(lambda x: int(x), list(polies.replace("\n", ""))))
            s_row.append(polinome)
        s.append(s_row)

    while True:
        raw_x = input("Enter x: ")
        x = []
        if mod == 2:
            x.append(list(map(lambda y: int(y), raw_s.split(" "))))
        else:
            x_row = []
            for polies in raw_x.split(" "):
                polinome = list(map(lambda y: int(y), list(polies.replace("\n", ""))))
                x_row.append(polinome)
            x.append(x_row)

        print("Next state: ")
        matrix_row = fun(s, A, x, B)
        matrix_print(matrix_row)
        print("Next output: ")
        matrix_print(fun(s, C, x, D))
        s = matrix_row

# def test_main():
#     global mod
#     op1 = list(map(lambda x: int(x), input().split(" ")))
#     op2 = list(map(lambda x: int(x), input().split(" ")))
#     mod = list(map(lambda x: int(x), input().split(" ")))
#
#     # print(op1)
#     # print(op2)
#
#     print(mult_mod(op1, op2))


if __name__ == "__main__":
    main()
