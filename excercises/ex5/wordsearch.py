import os
import sys

MATRIX_MODEL = list[list[str]]
COUNTER_MODEL = list[tuple[str, int]]


def read_wordlist(filename: str) -> list[str]:
    """
    Reads a text file containing a list of words and returns its contents as a list of strings.
    :param filename: The name of the file to be read, containing the list of words.
    :return: A list of strings, where each string is a word from the file.
    """
    with open(filename, "r") as file:
        return file.read().splitlines()


def read_matrix(filename: str) -> list[list[str]]:
    """
    Reads a matrix from a file and returns the matrix as a list of lists.
    :param filename: The path to the file containing the matrix.
    :return: Matrix as a list of lists.
    """
    with open(filename, "r") as file:
        matrix = [line.split(",") for line in file.read().splitlines()]
        return matrix


def print_matrix(matrix: MATRIX_MODEL):
    """
    Prints a matrix nicely.
    :param matrix: Matrix
    """
    for row in matrix:
        for letter in row:
            print(letter, end="    ")
        print("\n")


def up_strings(matrix: MATRIX_MODEL) -> list[str]:
    """
    Creates up strings from a matrix.
    :param matrix: Matrix
    :return: list of strings representing columns upwards.
    """
    cols_up = []
    for col in range(len(matrix) - 1):
        cols_up.append('')
        for row in matrix[::-1]:
            cols_up[col] += row[col]
    return cols_up


def down_strings(matrix: MATRIX_MODEL) -> list[str]:
    """
    Creates down strings from a matrix.
    :param matrix: Matrix
    :return: list of strings representing columns downwards.
    """
    cols_down = []
    for col in range(len(matrix) - 1):
        cols_down.append('')
        for row in matrix:
            cols_down[col] += row[col]
    return cols_down


def right_strings(matrix: MATRIX_MODEL) -> list[str]:
    """
    Creates right strings from a matrix.
    :param matrix: Matrix
    :return: list of strings representing rows rightwards.
    """
    return [''.join(row) for row in matrix]


def left_strings(matrix: MATRIX_MODEL) -> list[str]:
    """
    Creates left strings from a matrix.
    :param matrix: Matrix
    :return: list of strings representing rows leftwards.
    """
    return [''.join(row[::-1]) for row in matrix]


def upright_diagonal_strings(matrix: MATRIX_MODEL) -> list[str]:
    """
    Creates upright diagonal strings from a matrix.
    :param matrix: Matrx
    :return: list of strings representing diagonals uprightwards.
    """
    rows, cols = len(matrix), len(matrix[0])
    diagonals = []
    starting_row, starting_col = 0, 0
    while starting_col < cols:
        diagonals.append('')
        row, col = starting_row, starting_col
        while row >= 0 and col < cols:
            diagonals[len(diagonals) - 1] += matrix[row][col]
            row -= 1
            col += 1
        starting_row = starting_row + 1 if len(diagonals) < rows else rows - 1
        starting_col = 0 if len(diagonals) < rows else starting_col + 1
    return diagonals


def upleft_diagonal_strings(matrix: MATRIX_MODEL) -> list[str]:
    """
    Creates upleft diagonal strings from a matrix.
    :param matrix: Matrx
    :return: list of strings representing diagonals upleftwards.
    """
    rows, cols = len(matrix), len(matrix[0])
    diagonals = []
    starting_row, starting_col = rows - 1, 0
    while starting_row >= 0:
        diagonals.append('')
        row, col = starting_row, starting_col
        while row >= 0 and col >= 0:
            diagonals[len(diagonals) - 1] += matrix[row][col]
            row -= 1
            col -= 1
        starting_row = rows - 1 if len(diagonals) < cols else starting_row - 1
        starting_col = starting_col + 1 if len(diagonals) < cols else cols - 1
    return diagonals


def downright_diagonal_strings(matrix: MATRIX_MODEL) -> list[str]:
    """
    Creates downright diagonal strings from a matrix.
    :param matrix: Matrx
    :return: list of strings representing diagonals downrightwards.
    """
    rows, cols = len(matrix), len(matrix[0])
    diagonals = []
    starting_row, starting_col = 0, cols - 1
    while starting_row < rows:
        diagonals.append('')
        row, col = starting_row, starting_col
        while row < rows and col < cols:
            diagonals[len(diagonals) - 1] += matrix[row][col]
            row += 1
            col += 1
        starting_row = 0 if len(diagonals) < cols else starting_row + 1
        starting_col = starting_col - 1 if len(diagonals) < cols else 0
    return diagonals


def downleft_diagonal_strings(matrix: MATRIX_MODEL) -> list[str]:
    """
    Creates downleft diagonal strings from a matrix.
    :param matrix: Matrx
    :return: list of strings representing diagonals downleftwards.
    """
    rows, cols = len(matrix), len(matrix[0])
    diagonals = []
    starting_row, starting_col = rows - 1, cols - 1
    while starting_col >= 0:
        diagonals.append('')
        row, col = starting_row, starting_col
        while row < rows and col >= 0:
            diagonals[len(diagonals) - 1] += matrix[row][col]
            row += 1
            col -= 1
        starting_row = starting_row - 1 if len(diagonals) < rows else 0
        starting_col = cols - 1 if len(diagonals) < rows else starting_col - 1
    return diagonals


DIRECTIONS_TO_FUNCTIONS = {
    "u": up_strings,
    "d": down_strings,
    "r": right_strings,
    "l": left_strings,
    "w": upright_diagonal_strings,
    "x": upleft_diagonal_strings,
    "y": downright_diagonal_strings,
    "z": downleft_diagonal_strings
}


def count_instances_of_string(string: str, string_to_count: str) -> int:
    """
    Counts the instances of a given string with overlap.
    :param string: Original string.
    :param string_to_count: String to count.
    :return:
    """
    instances = 0
    for i in range(len(string) - len(string_to_count) + 1):
        if string[i:i + len(string_to_count)] == string_to_count:
            instances += 1
    return instances


def find_words(word_list: list[str],
               matrix: list[list[str]],
               directions: str) -> COUNTER_MODEL:
    """
    Search for a list of words in a matrix and returns how many times each word is in the matrix.
    :param word_list: Words to find in word-search.
    :param matrix: The word-search as a list of lists.
    :param directions: Directions to look the words.
    :return: List of tuples representing how many times each word is in the word-search
    """
    strings_to_search = []
    for direction in directions:
        strings_to_search.extend(DIRECTIONS_TO_FUNCTIONS[direction.lower()](matrix))
    words_count = []
    for word in word_list:
        counter = 0
        for string in strings_to_search:
            counter += count_instances_of_string(string, word)
        if counter > 0:
            words_count.append((word, counter))
    return words_count


def write_output(results: COUNTER_MODEL, filename: str) -> None:
    """
    Writes results to a text file.
    :param results: List of tuples representing how many times each word is in the word-search
    :param filename: Name of the file to write.
    """
    with open(filename, "w") as file:
        for word, count in results:
            file.write(f"{word},{count}" + "\n")


def main(word_file: str,
         matrix_file: str,
         output_file: str,
         directions: str) -> None:
    words = read_wordlist(word_file)
    matrix = read_matrix(matrix_file)
    results = find_words(words, matrix, directions)
    write_output(results, output_file)


if __name__ == '__main__':
    arguments = sys.argv[1:]
    if len(arguments) != 4:
        print("You need to insert 4 inputs.")
        sys.exit()
    if not os.path.isfile(arguments[0]):
        print("Words file does not exist.")
        sys.exit()
    if not os.path.isfile(arguments[1]):
        print("Matrix file does not exist.")
        sys.exit()
    if not arguments[2].endswith(".txt"):
        print("Matrix file must end with '.txt'.")
        sys.exit()
    for direction in arguments[3]:
        if direction not in DIRECTIONS_TO_FUNCTIONS.keys():
            print("Direction '" + direction + "' is not supported.")
            sys.exit()
    main(arguments[0], arguments[1], arguments[2], ''.join(set(arguments[3])))
