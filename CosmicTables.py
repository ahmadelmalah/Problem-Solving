params = input().split()
rows = int(params[0])
columns = int(params[1])
operations = int(params[2])

table = []
for i in range(rows):
    row = input().split()
    row = [int(x) for x in row]
    table.append(row)

original_index_columns = list(range(columns))
original_index_rows = list(range(rows))
for i in range(operations):
    operation_params = input().split()
    operation = operation_params[0]
    x = int(operation_params[1])-1
    y = int(operation_params[2])-1

    if operation == 'g':
        original_x = original_index_rows[x]
        original_y = original_index_columns[y]
        print(table[original_x][original_y])
    elif operation == 'r':
        temp = original_index_rows[x]
        original_index_rows[x] = original_index_rows[y]
        original_index_rows[y] = temp
    else:
        temp = original_index_columns[x]
        original_index_columns[x] = original_index_columns[y]
        original_index_columns[y] = temp