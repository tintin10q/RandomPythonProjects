# Name: Quinten Cabo
# Student number: u789241

def highestcolumn(matrix):
    matrix = switch(matrix)
    output = 0
    for row in matrix:
        output += max(row)
    return output


def switch(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_matrix_part = []
        for row in matrix:
            new_matrix_part.append(row[i])
        new_matrix.append(new_matrix_part[:])
    return new_matrix


def main():
    print(highestcolumn([[1, 5, 8, 2, 5], [3, 6, 9, 1, 4], [1, 5, 1, 4, 3], [9, 2, 6, 3, 1]]))  # 33
    print(highestcolumn([[1, 2, 3, 4, 5, 6, 7, 8, 9]]))  # 45
    print(highestcolumn([[1], [2], [3], [4], [5], [6], [7], [8], [9]]))  # 9
    print(highestcolumn([[1]]))  # 1


if __name__ == "__main__":
    main()
