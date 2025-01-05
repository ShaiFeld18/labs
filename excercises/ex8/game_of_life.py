import numpy
import numpy as np

board_type = np.ndarray
loc_type = tuple[int, int]


def get_alive_neighbours(board: board_type) -> board_type:
    padded_board = np.pad(board, pad_width=1, mode='constant', constant_values=0)
    return (
            padded_board[:-2, :-2] + padded_board[:-2, 1:-1] + padded_board[:-2, 2:] +
            padded_board[1:-1, :-2] + padded_board[1:-1, 2:] +
            padded_board[2:, :-2] + padded_board[2:, 1:-1] + padded_board[2:, 2:]
    )


def is_alive(cell: int, alive_neighbours: int) -> bool:
    if (cell == 1 and alive_neighbours in [2, 3]) or (cell == 0 and alive_neighbours == 3):
        return True
    return False


def game_of_life(board: board_type, gen_num: int) -> board_type:
    for _ in range(gen_num):
        alive_neighbours = get_alive_neighbours(board)
        next_gen = np.ndarray(shape=board.shape, dtype=board_type)
        for idx, cell in np.ndenumerate(board):
            next_gen[idx] = is_alive(cell, alive_neighbours[idx])
        board = next_gen.astype(int)
    return board


def game_of_life_kernel(board: numpy.ndarray, kernel: numpy.ndarray, gen_num: int,
                        life_threshold=2, overcrowding_threshold=4) -> numpy.ndarray:
    pass


if __name__ == '__main__':
    board = np.array([[0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]])
    gen_num = 500
    print(game_of_life(board, gen_num))
    # Output:
    # [[0 0 0 0 0 0]
    # [0 0 0 1 1 0]
    # [0 0 1 0 0 1]
    # [0 0 0 1 1 0]
    # [0 0 0 0 0 0]
    # [0 0 0 0 0 0]]
