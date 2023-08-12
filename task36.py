def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        oper = []
        for j in range(1, num_columns + 1):
            oper.append(operation(i, j))
        print(''.join(f'{i:>3}' for i in oper))


print_operation_table(lambda x, y: x * y)