# write your code here
def print_matrix(matrix):
    print("-" * 9)
    for y in range(3):
        print("| ", end="")
        for x in range(3):
            print(matrix[x][y], end=" ")
        print("|")
    print("-" * 9)

#cells = input("Enter cells: ")
matrix = [[" " for j in range(3)] for i in range(3)]
#for y in range(3):
#    for x in range(3):
#        matrix[x][y] = cells[y * 3 + x]

print_matrix(matrix)

correct_coords = False
winner = None
steps = ["X", "O"]
k = 0
while winner == None:
    while correct_coords != True:
        coords = input("Enter the coordinates: ").split()
        if not (coords[0].isdigit() and coords[1].isdigit()):
            print("You should enter numbers!")
        elif not (1 <= int(coords[0]) <= 3 and 1 <= int(coords[1]) <= 3):
            print("Coordinates should be from 1 to 3!")
        elif matrix[int(coords[0]) - 1][3 - int(coords[1])] != " ":
            print(matrix[int(coords[0]) - 1][3 - int(coords[1])])
            print("This cell is occupied! Choose another one!")
        else:
            correct_coords = True
    matrix[int(coords[0]) - 1][3 - int(coords[1])] = steps[k]
    print_matrix(matrix)
    correct_coords = False
    # проверка столбцов
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != " ":
            winner = matrix[i][0]
            break
    # проверка строк
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != " ":
            winner = matrix[0][i]
            break
    # проверка диагоналей
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != " " or matrix[0][2] == matrix[1][1] == matrix[2][0] != " ":
        # print(f"{matrix[1][1]} wins")
        winner = matrix[1][1]
        break
    k = (k + 1) % 2
    if not any(y for x in matrix for y in x if y == " "):
        winner = "Draw"
        break
print(f"{winner} wins" if winner != "Draw" else winner)
