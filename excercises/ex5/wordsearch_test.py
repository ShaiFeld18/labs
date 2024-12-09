from excercises.ex5.wordsearch import read_wordlist, read_matrix, find_words


def test_read_wordlist() -> None:
    assert read_wordlist("word_list.txt") == ["dog",
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


def test_read_matrix() -> None:
    assert read_matrix("mat.txt") == [['a', 'p', 'p', 'l', 'e'],
                                      ['a', 'g', 'o', 'd', 'o'],
                                      ['n', 'n', 'e', 'r', 't'],
                                      ['g', 'a', 'T', 'A', 'C'],
                                      ['m', 'i', 'c', 's', 'r'],
                                      ['P', 'o', 'P', 'o', 'P']]


def test_find_words_longer_than_matrix() -> None:
    matrix = read_matrix("mat.txt")
    long_word = ''.join(["a" for _ in range(max(len(matrix), len(matrix[0])))])
    assert find_words([long_word], matrix, "udlrwxyz") == []


def test_find_words_repeated_multiple_times() -> None:
    matrix = read_matrix("mat.txt")
    assert find_words(["PoP"], matrix, "udlrwxyz") == [("PoP", 4)]


def test_find_words_no_matches() -> None:
    matrix = read_matrix("mat.txt")
    assert find_words(["PoP"], matrix, "w") == []
