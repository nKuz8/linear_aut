def matrix_mult(matrix_1, matrix_2):
    if matrix_check(matrix_1, matrix_2, "mult"):
        return 0
    else:
        result_matrix = []
        result_row = []
        resul_mult = 0

        for i in range(0, len(matrix_1)):
            for j in range(0, len(matrix_2[0])):
                for k in range(0, len(matrix_1[0])):
                    resul_mult = add_mod(mult_mod(matrix_1[i][k], matrix_2[k][j]), resul_mult)
                result_row.append(resul_mult)
                resul_mult = 0
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
                result_row.append(add_mod(matrix_1[i][j], matrix_2[i][j]))
            result_matrix.append(result_row)
            result_row = []

        return result_matrix


def matrix_print(matrix):
    for row in matrix:
        for el in row:
            print("{} ".format(el), end = "")
        print()
    print("\n")


def add_mod(op1, op2):
    return (op1 + op2) % mod


def mult_mod(op1, op2):
    return (op1 * op2) % mod


def fun(s, matrix_A, x, matrix_B):
    return matrix_add(matrix_mult(s, matrix_A), matrix_mult(x, matrix_B))


def main():
    s = []
    s.append(list(map(lambda x : int(x), input("Enter s0: ").split(" "))))

    print("Enter matrix A: ")
    matrix_A = []
    matrix_row = []
    while True:
        raw_input = input()
        if raw_input == "q":
            break
        else:
            matrix_row = list(map(lambda x : int(x), raw_input.split(" ")))
            matrix_A.append(matrix_row)

    matrix_B = []
    print("Enter matrix B: ")
    while True:
        raw_input = input()
        if raw_input == "q":
            break
        else:
            matrix_row = list(map(lambda x : int(x), raw_input.split(" ")))
            matrix_B.append(matrix_row)

    matrix_C = []
    print("Enter matrix C: ")
    while True:
        raw_input = input()
        if raw_input == "q":
            break
        else:
            matrix_row = list(map(lambda x : int(x), raw_input.split(" ")))
            matrix_C.append(matrix_row)

    matrix_D = []
    print("Enter matrix D: ")
    while True:
        raw_input = input()
        if raw_input == "q":
            break
        else:
            matrix_row = list(map(lambda x : int(x), raw_input.split(" ")))
            matrix_D.append(matrix_row)

    global mod
    mod = int(input("Enter mod: "))
    # matrix_print(matrix_add(matrix_mult(matrix_1, matrix_2), matrix_1))

    while True:
        x = []
        raw_input = input("Enter x: ")
        if raw_input == "q":
            break
        else:
            x.append(list(map(lambda x : int(x), raw_input.split(" "))))

            print("Next state: ")
            matrix_row = fun(s, matrix_A, x, matrix_B)
            matrix_print(matrix_row)
            print("Next output: ")
            matrix_print(fun(s, matrix_C, x, matrix_D))
            s = matrix_row


if __name__ == "__main__":
    main()
