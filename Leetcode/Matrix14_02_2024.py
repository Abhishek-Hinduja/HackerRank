matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

element =  matrix[1][2]
print(element)

count = 0
for row in matrix:
    for element in row:
        print(element, end = " ")
    print()

new_row = [2,5,8]
matrix.append(new_row)
print(matrix)

new_column_value = 20
for row in matrix:
    row.append(new_column_value)

print(matrix)

column_index_to_delete = 1
for row in matrix:
    del row[column_index_to_delete]

print(matrix)