import helper
from helper import SHIP, WATER, HIT_SHIP, HIT_WATER

board_model = list[list[int]]
game_model = tuple[board_model, board_model]
location_model = tuple[int, int]


def init_board(rows: int, columns: int) -> board_model:
    """Creates a board with all cells as water."""
    board = []
    for row in range(rows):
        row = [WATER for _ in range(columns)]
        board.append(row)
    return board


def valid_ship(board: board_model, size: int, loc: location_model) -> bool:
    """
    Checks if a boat can be placed in a specific location by two parameters:
    1) Checks if it is in the bounds of board
    2) The ship doesn't collide with other ships
    Return True if the location is valid and False otherwise.
    """
    row, col = loc

    # Check that the ship is in bounds of board
    if row + size - 1 > len(board) - 1 or col > len(board[0]) - 1:
        return False

    # Check there aren't ships in location
    for i in range(size):
        if board[row + i][col] != WATER:
            return False

    return True


def cell_name_to_loc(name: str) -> location_model:
    """Converts a cell name as a string with a letter and a number and returns a tuple with (row, col)"""
    row_num = name[1:]
    col_letter = name[0].upper()
    col_num = ord(col_letter) - ord('A')
    return int(row_num) - 1, col_num


def place_ship_in_board(board: board_model, ship_size: int, loc: location_model) -> board_model:
    """Places a ship in a board"""
    for i in range(ship_size):
        board[loc[0] + i][loc[1]] = helper.SHIP
    return board


def create_player_board(rows: int, columns: int, ship_sizes: list[int]) -> board_model:
    """This function creates a new board and lets the player place their ships"""
    board = init_board(rows, columns)
    ships_placed = 0
    while ships_placed < len(ship_sizes):
        helper.show_board(board)
        place = helper.get_input(f"Where do you want to place the ship? (size: {ship_sizes[ships_placed]})").upper()

        # Check if the location is in format
        if not helper.is_cell_name(place):
            helper.show_msg("The format of the provided location isn't valid. Try Again :)")
            continue
        loc = cell_name_to_loc(place)

        # Check if the location is valid
        if not valid_ship(board, ship_sizes[ships_placed], loc):
            helper.show_msg("The ship can't be placed in provided location. Try Again :)")
            continue

        board = place_ship_in_board(board, ship_sizes[ships_placed], loc)

        ships_placed += 1

    return board


def find_available_locations(board: board_model, ship_size: int) -> set[tuple[int, int]]:
    """Finds all locations where a ship of a given size can be placed."""
    available_locations = set([(row, col)
                               for row in range(len(board))
                               for col in range(len(board[0]))
                               if valid_ship(board, ship_size, (row, col))
                               ])
    return available_locations


def create_computer_board(rows: int, columns: int, ship_sizes: list[int]) -> board_model:
    """This function creates a new board and lets the computer place ships"""
    board = init_board(rows, columns)

    for size in ship_sizes:
        available_locations = find_available_locations(board, size)
        loc = helper.choose_ship_location(board, size, available_locations)
        board = place_ship_in_board(board, size, loc)

    return board


def create_new_game(num_rows: int, num_cols: int, ships_sizes: list[int]) -> game_model:
    """Returns a tuple with a player board and a computer board."""
    player_board = create_player_board(num_rows, num_cols, ships_sizes)
    computer_board = create_computer_board(num_rows, num_cols, ships_sizes)
    return player_board, computer_board


def hide_board(board: board_model) -> board_model:
    hidden_board = []
    for row in range(len(board)):
        hidden_board.append([])
        for col in range(len(board[0])):
            if board[row][col] == SHIP:
                hidden_board[row].append(WATER)
            else:
                hidden_board[row].append(board[row][col])
    return hidden_board


def find_valid_targets(board: board_model) -> set[location_model]:
    valid_targets = set([(row, col) for row in range(len(board)) for col in range(len(board[0]))
                         if board[row][col] not in [HIT_SHIP, HIT_WATER]])
    return valid_targets


def choose_targets(game: game_model) -> tuple[location_model, location_model]:
    """The player and the computer choose a target each."""
    valid_target = False
    while not valid_target:
        torpedo_loc = helper.get_input("Where do you want to attack?")
        if helper.is_cell_name(torpedo_loc):
            player_target = cell_name_to_loc(torpedo_loc)
        else:
            helper.show_msg("The format of the provided location isn't valid. Try Again :)")
            continue
        if player_target[0] > len(game[0]) - 1 or player_target[1] > len(game[0][0]) - 1:
            helper.show_msg("The location you provided is out of the board, try again.")
            continue
        if game[1][player_target[0]][player_target[1]] in [WATER, SHIP]:
            valid_target = True
        else:
            helper.show_msg("You can't attack a revealed square!")
    computer_target = helper.choose_torpedo_target(game[0], find_valid_targets(game[0]))
    return player_target, computer_target


def attack(board: board_model, target: tuple[int, int]) -> board_model:
    """Gets a board and a target and attack it."""
    if board[target[0]][target[1]] == SHIP:
        board[target[0]][target[1]] = HIT_SHIP
    else:
        board[target[0]][target[1]] = HIT_WATER
    return board


def is_over(game: game_model, ships_sizes: list[int]) -> bool:
    """Check if all the ships where hit in one of the boards."""
    squares_with_ships = sum(ships_sizes)
    for board in game:
        hit_ship_squares = 0
        for row in board:
            for square in row:
                if square == HIT_SHIP:
                    hit_ship_squares += 1
        if hit_ship_squares == squares_with_ships:
            return True
    return False


def main():
    keep_playing = True
    while keep_playing:
        # Create a new game
        num_rows, num_cols, ships_sizes = helper.NUM_ROWS, helper.NUM_COLUMNS, helper.SHIP_SIZES
        game = create_new_game(num_rows, num_cols, ships_sizes)

        # Run the game
        while not is_over(game, ships_sizes):
            helper.show_board(game[0], hide_board(game[1]))
            player_target, computer_target = choose_targets(game)
            game = (attack(game[0], computer_target), attack(game[1], player_target))
        helper.show_board(*game)

        # Ask if play again
        play_again = None
        while play_again not in ['Y', 'N']:
            play_again = helper.get_input("Do you want to play again? (Y\\N)")
        keep_playing = False if play_again == 'N' else True
