A = []
B = []
C = []
D = []
mod = 0


def matrix_mult(matrix_1, matrix_2):
    if matrix_check(matrix_1, matrix_2, "mult"):
        return 0
    else:
        result_matrix = []
        result_row = []
        result_mult = 0
        #print("multiple of {} on {}".format(matrix_1, matrix_2))

        for i in range(0, len(matrix_1)):
            for j in range(0, len(matrix_2[0])):
                for k in range(0, len(matrix_1[0])):
                    result_mult = add_mod(mult_mod(matrix_1[i][k], matrix_2[k][j]), result_mult, carry=True)
                result_row.append(result_mult)
                result_mult = 0
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
    return (op1 + op2) % mod
    if(False):
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
    return op1 % mod
    if(False):
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
    return (op1*op2) % mod
    if(False):
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


def dec_to_q(number, length):
    global mod
    res_vec = []
    for i in range(length):
        res_vec.append(number % mod)
        number //= mod
    res_vec.reverse()
    return [res_vec]


def q_to_dec(vec):
    number = 0
    for i in range(len(vec[0]) - 1, -1, -1):
        number += mod ** (len(vec[0]) - 1 - i) * vec[0][i]
    return number


def make_reach_table():
    global mod, A, B
    reach_table = []
    table_line = [0] * (mod ** len(A))
    for i in range(mod ** len(A)):
        for j in range(mod ** len(B)):
            table_line[q_to_dec(fun(dec_to_q(i, len(A)), A, dec_to_q(j, len(B)), B))] = 1
        reach_table.append(table_line)
        table_line = [0] * mod ** len(A)
    return reach_table

                       
def depth_first_search(reach_table, mode):
    global n
    stack = []
    marked = []
    result = []
    
    if mode == "strong":
        dps_rec(reach_table, 0, marked, stack, result, "strong") 
    for i in range(len(reach_table)):
        if mode == "strong" and i != 0:
            first = marked.copy()
            marked = []
            stack = []
            result = []
            dps_rec(reach_table, i, marked, stack, result, "strong")
            if first != marked:
                return False
            
        elif mode == "strong" and i == 0:
            continue

        else:
            flag = False
            for item in result:
                if i in item:
                    flag = True
                    break

            if flag:
                continue
            else:
                marked.append(i)
                stack.append(i)

                while len(stack) != 0:
                    for j in range(len(reach_table[i])):
                        if ((reach_table[i][j] == 1 or reach_table[j][i] == 1) and mode == "normal") and i != j:
                            flag = False
                            for item in result:
                                if j in item:
                                    flag = True
                                    break

                            if flag or j in marked:
                                continue
                            else:
                                marked.append(j)
                                stack.append(j)
                                dps_rec(reach_table, j, marked, stack, result, mode)
                                stack.pop(-1)
                    stack.pop(-1)

                result.append(marked)
                marked = []
    return result if mode == "normal" else True


def dps_rec(reach_table, i, marked, stack, result, mode):
    for j in range(len(reach_table[i])):
        if (((reach_table[i][j] == 1 or reach_table[j][i] == 1) and mode == "normal") or (reach_table[i][j] == 1 and mode == "strong")) and i != j:
            flag = False
            for item in result:
                if j in item:
                    flag = True
                    break

            if flag or j in marked:
                continue
            else:
                marked.append(j)
                stack.append(j)
                dps_rec(reach_table, j, marked, stack, result, mode)
                stack.pop(-1)


def main():
    global mod, A, B, C, D
    read_flags = [False] * 4
    polinome = []
    matrix_row = []

    f = input("Enter file name: ")
    with open(f, 'r') as file:
        global mod
        for line in file:
            if line[0] == "q":
                mod = int(line[line.find("=") + 1: ])
                print(mod)
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
                matrix_row = list(map(lambda x: int(x), line.replace("\n", "").split(" ")))
                A.append(matrix_row)
            elif read_flags[1]:
                matrix_row = list(map(lambda x: int(x), line.replace("\n", "").split(" ")))
                B.append(matrix_row)
            elif read_flags[2]:
                matrix_row = list(map(lambda x: int(x), line.replace("\n", "").split(" ")))
                C.append(matrix_row)
            elif read_flags[3]:
                matrix_row = list(map(lambda x: int(x), line.replace("\n", "").split(" ")))
                D.append(matrix_row)

    reach_table = make_reach_table()                        
    links = depth_first_search(reach_table, "normal")
    print("Automat is linked") if len(links) == 1 else print("Automat is not linked")
    print("Linked components: {}".format(links))
    print("Total links: {}".format(len(links)))
    strong_links = depth_first_search(reach_table, "strong")
    print("Automat is strongly linked") if strong_links else print("Automat is not strongly linked")                        
    raw_s = input("Enter s0: ")
    s = [list(map(lambda x: int(x), raw_s.replace("\n", "").split(" ")))]
    # if type(mod) is int:
    #     s.append(list(map(lambda x: int(x), raw_s.split(" "))))
    # else:

    while True:
        raw_x = input("Enter x: ")
        x = [list(map(lambda x: int(x), raw_x.replace("\n", "").split(" ")))]

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
