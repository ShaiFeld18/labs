from wordsearch import read_wordlist, read_matrix, find_words

WORDS_LIST = ["dog",
              "CAT",
              "cAt",
              "anTs",
              "apple",
              "cake",
              "long",
              "short",
              "can",
              "toe",
              "poeT",
              "Crop",
              "one",
              "two",
              "three",
              "four",
              "five",
              "six",
              "seven",
              "eight",
              "nine",
              "ten",
              "PoP",
              "pole",
              "raw",
              "red",
              "blue",
              "move",
              "gum",
              "son",
              "shoe",
              "she",
              "he",
              "bye"]
MATRIX = [['a', 'p', 'p', 'l', 'e'],
          ['a', 'g', 'o', 'd', 'o'],
          ['n', 'n', 'e', 'r', 't'],
          ['g', 'a', 'T', 'A', 'C'],
          ['m', 'i', 'c', 's', 'r'],
          ['P', 'o', 'P', 'o', 'P']]


def test_read_wordlist() -> None:
    file_name = "wordlist_test.txt"
    with open(file_name, "w") as file:
        file.write("\n".join(WORDS_LIST))
    assert read_wordlist(file_name) == WORDS_LIST


def test_read_matrix() -> None:
    file_name = "matrix_test.txt"
    with open(file_name, "w") as file:
        for row in MATRIX:
            file.write(",".join(row) + "\n")
    assert read_matrix("mat.txt") == MATRIX


def test_find_words_longer_than_matrix() -> None:
    long_word = ''.join(["a" for _ in range(max(len(MATRIX), len(MATRIX[0])))])
    assert find_words([long_word], MATRIX, "udlrwxyz") == []


def test_find_words_repeated_multiple_times() -> None:
    assert find_words(["PoP"], MATRIX, "udlrwxyz") == [("PoP", 4)]


def test_find_words_no_matches() -> None:
    assert find_words(["PoP"], MATRIX, "w") == []
