import numpy as np


def print_matrix(matrix):
    print("resultant")
    print(np.array(matrix))
    print()


def get_input(matrix_number):
    print(f"enter to dimension a  matrix ")
    rows = int(input("number of rows"))
    cols = int(input("number of columns"))

    matrix = []
    print(f"enter the elements of  matrix row by row")
    for i in range(rows):
        row = list(map(int, input(f"row {i+1}:").split()))
        matrix.append(row)
    return np.array(matrix)


def addition(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        print("matrix must have the same dimensions for addition")
        return None
    return matrix1 + matrix2


def subtraction(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        print("matrix must have the same dimensions for addition")
        return None
    return matrix1 - matrix2


def multiplication(matrix1, matrix2):
    if matrix1.shape[1] != matrix2.shape[0]:
        print(
            "number  of columns in matrix1 must be equal to  number of rows in matrix2 "
        )
        return None
    return np.dot(matrix1, matrix2)


def transpose_m(matrix):
    return np.transpose(matrix)


def determinant_m(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        print("only applicable for square  matrix")
        return None
    return np.linalg.det(matrix)


def display_option():
    print("operations")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.Transpose")
    print("5.determinant")
    print("6.exit")


def main():
    while True:
        display_option()
        choice = input("select from 1 to 6\n")

        if choice == "1":
            matrix1 = get_input(1)
            matrix2 = get_input(2)
            result = addition(matrix1, matrix2)
            if result is not None:
                print_matrix(result)

        elif choice == "2":
            matrix1 = get_input(1)
            matrix2 = get_input(2)
            result = subtraction(matrix1, matrix2)
            if result is not None:
                print_matrix(result)

        elif choice == "3":
            matrix1 = get_input(1)
            matrix2 = get_input(2)
            result = multiplication(matrix1, matrix2)
            if result is not None:
                print_matrix(result)

        elif choice == "4":
            matrix = get_input(1)
            result = transpose_m(matrix)
            print_matrix("Transpose is " + result)

        elif choice == "5":
            matrix = get_input(1)
            result = determinant_m(matrix)
            if result is not None:
                print(f"determinant:{result}")

        elif choice == "6":
            print("exiting from the program")
            break

        else:
            print("invalid choice")


if __name__ == "__main__":
    main()
