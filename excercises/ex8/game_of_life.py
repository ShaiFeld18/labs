import numpy as np

board_type = np.ndarray
loc_type = tuple[int, int]


def get_alive_neighbours(board: board_type) -> np.ndarray:
    """
    Check how many live cells has each cell in the board.
    :param board: Game of Life board
    :return: matrix with the number of living cells of each cell in the board.
    """
    padded_board = np.pad(board, pad_width=1, mode='constant', constant_values=0)
    return (
            padded_board[:-2, :-2] + padded_board[:-2, 1:-1] + padded_board[:-2, 2:] +
            padded_board[1:-1, :-2] + padded_board[1:-1, 2:] +
            padded_board[2:, :-2] + padded_board[2:, 1:-1] + padded_board[2:, 2:]
    )


def is_alive(cell_val: int, alive_neighbours: int) -> bool:
    """
    Checks if a cell needs to be alive in the next generation by the rules of the game.
    :param cell_val: current value of the cell.
    :param alive_neighbours: living neighbors of the cell.
    :return: boolean alive or not
    """
    if (cell_val == 1 and alive_neighbours in [2, 3]) or (cell_val == 0 and alive_neighbours == 3):
        return True
    return False


def game_of_life(board: board_type, gen_num: int) -> board_type:
    """
    Simulates the Game of Life.
    :param board: starting board.
    :param gen_num: numbers of generations to simulate.
    :return: board after the simulation.
    """
    for _ in range(gen_num):
        alive_neighbours = get_alive_neighbours(board)
        next_gen = np.ndarray(shape=board.shape, dtype=board_type)
        for idx, cell in np.ndenumerate(board):
            next_gen[idx] = is_alive(cell, alive_neighbours[idx])
        board = next_gen.astype(int)
    return board


def apply_kernel(board: board_type, kernel: board_type) -> board_type:
    """
    Apply a kernel to a board.
    :param board: matrix
    :param kernel: kernel to apply
    :return: matrix after applying kernel
    """
    padded_board = np.pad(board, pad_width=1, mode='constant', constant_values=0)
    results = np.zeros(shape=board.shape, dtype=board_type)
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            curr_zone = padded_board[row:row + kernel.shape[0], col:col + kernel.shape[1]]
            results[row][col] = np.sum(curr_zone * kernel)
    return results


def is_alive_kernel(cell_value: int,
                    score: int,
                    life_threshold: int,
                    overcrowding_threshold: int) -> int:
    """
    Checks if a cell is alive or not by the rules of the game.
    :param cell_value: current value of cell.
    :param score: score of the cell by the kernel.
    :param life_threshold: threshold of life cells
    :param overcrowding_threshold: threshold of overcrowding cells.
    :return: 1 for alive, 0 for dead.
    """
    if score < life_threshold:
        return 0
    elif score > overcrowding_threshold:
        return 0
    elif life_threshold < score <= overcrowding_threshold:
        return 1
    else:
        return cell_value


def game_of_life_kernel(board: board_type,
                        kernel: board_type,
                        gen_num: int,
                        life_threshold=2,
                        overcrowding_threshold=4) -> board_type:
    """
    Simulates the Game of Life.
    :param board: starting board.
    :param kernel: kernel to calculate score.
    :param gen_num: number of generations to simulate.
    :param life_threshold: threshold of life cells
    :param overcrowding_threshold: threshold of overcrowding cells.
    :return: board after the simulation.
    """
    for _ in range(gen_num):
        life_score = apply_kernel(board, kernel)
        next_gen = np.zeros_like(board, dtype=int)
        for idx, cell in np.ndenumerate(board):
            next_gen[idx] = is_alive_kernel(cell, life_score[idx], life_threshold, overcrowding_threshold)
        board = next_gen
    return board
