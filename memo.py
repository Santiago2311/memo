import random
import time
import os

SHOW = [["Z", "Z", "Z", "Z", "Z", "Z"], ["Z", "Z", "Z", "Z", "Z", "Z"], [
    "Z", "Z", "Z", "Z", "Z", "Z"], ["Z", "Z", "Z", "Z", "Z", "Z"], [
    "Z", "Z", "Z", "Z", "Z", "Z"], ["Z", "Z", "Z", "Z", "Z", "Z"]]
HIDDEN = [["A", "E", "D", "C", "G", "P"], ["J", "I", "D", "M", "H", "Q"], [
    "B", "K", "J", "K", "L", "Q"], ["F", "O", "I", "A", "F", "R"], [
    "G", "C", "L", "O", "N", "P"], ["E", "M", "H", "N", "B", "R"]]
PAIRS = 18

PUNCTUATION = 0

print("Welcome to the game. Good luck!!!")


def matrix(matriz):
    """
    Print a matrix that it recived as a parameter
    """
    for row in matriz:
        for elemento in row:
            print(elemento, end=" ")
        print()


def update_matrix(m, row, col, value):
    """
    Actualice the vales of the matrix
    """
    m[row][col] = value


def check_equalValues(m, row1, col1, row2, col2):
    """
        Validate that to cards are the same or not
    """
    if m[row1][col1] == m[row2][col2]:
        return True
    else:
        return False


def update_temp(s, h, r1, c1, r2, c2):
    """
    Function to update a value in temporary matrix
    """
    temp = [row[:] for row in s]
    temp[r1][c1] = h[r1][c1]
    temp[r2][c2] = h[r2][c2]
    return temp


def check_DiffX(m, row1, col1, row2, col2):
    """
    Function to check if the value of the card is different to X
    """
    if (m[row1][col1] != "X" and m[row2][col2] != "X"):
        return True
    else:
        return False


def update_pairs(pairs):
    """
    Function that modify the value of pairs in the matrix
    """
    pairs = pairs - 1
    return pairs


def check_validRC(row, col):
    """
    Check if the selected column and row are in the matrix dimensions
    """
    if (row < 0 or row > 5) or (col < 0 or col > 5):
        return False
    else:
        return True


def shuffle(m):
    """
    Suffle the cards in the matrix
    """
    flattened_matrix = [element for row in m for element in row]
    random.shuffle(flattened_matrix)

    shuffled_matrix = [
        flattened_matrix[i:i+6]  # Is a 6 x 6 matrix
        for i in range(0, len(flattened_matrix), 6)
    ]
    return shuffled_matrix


def trackmatrix():
    """
    It shows the hidden matrix and the normal matrix
    """
    os.system('cls')
    matrix(SHOW)
    print()
    # Uncomment to show the matrix with the answers
    matrix(hidden)
    print()


def check_validCards(r1, c1, r2, c2):
    """
    Validate if user do not select the same card
    """
    if (r1 == r2 and c1 == c2):
        return False
    else:
        return True


hidden = shuffle(HIDDEN)

trackmatrix()
while PAIRS > 0:
    r1 = int(input("Please enter r1: "))
    c1 = int(input("Please enter c1: "))
    r2 = int(input("Please enter r2: "))
    c2 = int(input("Please enter c2: "))

    if (check_validCards(r1, c1, r2, c2)):
        if (check_validRC(r1, c1) and check_validRC(r2, c2)):
            if (check_DiffX(SHOW, r1, c1, r2, c2)):
                temp = update_temp(SHOW, hidden, r1, c1, r2, c2)
                matrix(temp)
                time.sleep(5)
                os.system('cls')
                print()
                if (check_equalValues(hidden, r1, c1, r2, c2)):
                    PUNCTUATION += 1000
                    print("Encontraste un par, yay!\n")
                    print(f"Tu puntuación es: {PUNCTUATION}\n")
                    update_matrix(SHOW, r1, c1, "X")
                    update_matrix(SHOW, r2, c2, "X")
                    pairs = update_pairs(PAIRS)
                else:
                    puntuacion = PUNCTUATION - 500
                    print("No es un par, lo siento!\n")
                    print(f"Tu puntuación es: {puntuacion}\n")
            else:
                print("No es una carta valida\n")
        else:
            print("No es una fila o columna valida\n")
    else:
        print("No puedes seleccionar la misma tarjeta dos veces")

    time.sleep(2)
    trackmatrix()

print(f"Tu puntuación FINAL es: {PUNCTUATION}\n")
